# -*- coding: utf-8 -*-
import logging
from datetime import datetime

from src.structure.map import Map
from src.structure.string import String
from src.structure.template.template_factory_visitor import TemplateFactoryVisitor

logger = logging.getLogger(__name__)


def create_date_time_template():
    """DateTime Template
    Defines the format of the date time
    """
    iso_regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-' \
                r'(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):' \
                r'([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):' \
                r'[0-5][0-9])?$'
    template_map = Map()
    template_map[DateTime.DATE_TIME_KEY] = String(iso_regex)

    template_factory = TemplateFactoryVisitor()
    template = template_map.accept(template_factory)
    return template


class DateTime:
    """DateTime BaseType Class

    Helper class used by the date time view_model representing
    the actual type 'DateTime'.
    Can be used by other classes as a helper to be able to
    include date times in a overlaying datatype.
    """
    TEMPLATE = None
    DATE_TIME_KEY = 'date_time'
    ACCURACY_KEY = 'accuracy'

    def __init__(self, structure: Map = Map()):
        """DateTime Constructor

        Args:
            structure (Map): underlying map interpretation to
                which property calls are dispatched
        """
        if DateTime.DATE_TIME_KEY not in structure:
            default_time: datetime = datetime.min
            structure[DateTime.DATE_TIME_KEY] = String(default_time.isoformat())

        self._data: Map = structure

    @property
    def date_time(self) -> datetime:
        date_time_string: String = self._data[DateTime.DATE_TIME_KEY]
        try:
            value: datetime = datetime.fromisoformat(date_time_string.value)
        except ValueError:
            logger.error('could not parse date time format')
            value: datetime = datetime.min
        return value

    @date_time.setter
    def date_time(self, value: datetime):
        self._data[DateTime.DATE_TIME_KEY].value = value.isoformat()

    """
    # no easy conversion found.
    
    @property
    def accuracy(self):
        accuracy_string: String = self._data[DateTime.ACCURACY_KEY]
        return 

    @accuracy.setter
    def accuracy(self, value: timedelta):
        self._data[DateTime.ACCURACY_KEY] = value
    """


DateTime.TEMPLATE = create_date_time_template()
