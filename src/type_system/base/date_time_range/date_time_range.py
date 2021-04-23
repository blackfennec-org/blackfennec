# -*- coding: utf-8 -*-
import logging

from src.structure.map import Map
from src.structure.string import String
from datetime import datetime

logger = logging.getLogger(__name__)


def create_template():
    """DateTimeRange Template
    Defines the format of the date time range
    """
    iso_regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-' \
                r'(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):' \
                r'([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):' \
                r'[0-5][0-9])?$'

    logger.info('bidding on object')
    template = Map()
    template[DateTimeRange.START_KEY] = String(iso_regex)
    template[DateTimeRange.END_KEY] = String(iso_regex)
    return template


class DateTimeRange:
    TEMPLATE = None
    START_KEY = 'date_time_start'
    END_KEY = 'date_time_end'

    def __init__(self, structure: Map = Map()):
        """DateTimeRange Constructor

        Args:
            structure (Map): underlying map interpretation to
                which property calls are dispatched
        """
        if DateTimeRange.START_KEY not in structure:
            default_start_time: datetime = datetime.min
            structure[DateTimeRange.START_KEY] = String(default_start_time.isoformat())

        if DateTimeRange.END_KEY not in structure:
            default_end_time: datetime = datetime.max
            structure[DateTimeRange.END_KEY] = String(default_end_time.isoformat())

        self._data: Map = structure

    @property
    def date_time_start(self) -> datetime:
        date_time_start_string: String = self._data[DateTimeRange.START_KEY]
        try:
            value: datetime = datetime.fromisoformat(date_time_start_string.value)
        except ValueError:
            logger.error('could not parse start date time format')
            value: datetime = datetime.min
        return value

    @date_time_start.setter
    def date_time_start(self, value: datetime):
        self._data[DateTimeRange.START_KEY].value = value.isoformat()

    @property
    def date_time_end(self) -> datetime:
        date_time_end_string: String = self._data[DateTimeRange.END_KEY]
        try:
            value: datetime = datetime.fromisoformat(date_time_end_string.value)
        except ValueError:
            logger.error('could not parse end date time format')
            value: datetime = datetime.max
        return value

    @date_time_end.setter
    def date_time_end(self, value: datetime):
        self._data[DateTimeRange.END_KEY].value = value.isoformat()


DateTimeRange.TEMPLATE = create_template()
