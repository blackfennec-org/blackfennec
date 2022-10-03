# -*- coding: utf-8 -*-
import logging
from datetime import datetime

from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.black_fennec.structure.type.map_type import MapType
from src.black_fennec.structure.type.type_factory import TypeFactory

logger = logging.getLogger(__name__)


def create_date_time_type():
    """DateTime Type
    Defines the format of the date time
    """
    tf = TypeFactory()
    iso_regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-' \
                r'(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):' \
                r'([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):' \
                r'[0-5][0-9])?$'
    type = tf.create_map(type="DateTime", super=MapType(), properties={
        DateTime.DATE_TIME_KEY: tf.create_string(pattern=iso_regex)
    })

    return type


class DateTime:
    """DateTime BaseType Class

    Helper class used by the date time view_model representing
    the actual type 'DateTime'.
    Can be used by other classes as a helper to be able to
    include date times in a overlaying datatype.
    """
    TYPE = None
    DATE_TIME_KEY = 'date_time'
    ACCURACY_KEY = 'accuracy'

    def __init__(self, subject: Map = None):
        """DateTime Constructor

        Args:
            subject (Map): underlying map interpretation to
                which property calls are dispatched
        """
        self._subject: Map = subject or Map()
        if DateTime.DATE_TIME_KEY not in self.subject.value:
            default_time: datetime = datetime.min
            self.subject.add_item(
                DateTime.DATE_TIME_KEY,
                String(default_time.isoformat())
            )

    @property
    def subject(self):
        return self._subject

    def _get_value(self, key):
        if key not in self.subject.value:
            return None
        return self.subject.value[key].value

    def _set_value(self, key, value):
        assert key in self.subject.value
        self.subject.value[key].value = value

    @property
    def date_time(self) -> datetime:
        date_time_string = self._get_value(DateTime.DATE_TIME_KEY)
        try:
            value: datetime = datetime.fromisoformat(date_time_string)
        except ValueError:
            logger.error('could not deserialize date time format')
            value: datetime = datetime.min
        return value

    @date_time.setter
    def date_time(self, value: datetime):
        self._set_value(DateTime.DATE_TIME_KEY, value.isoformat())

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


DateTime.TYPE = create_date_time_type()
