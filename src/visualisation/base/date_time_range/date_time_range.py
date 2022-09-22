# -*- coding: utf-8 -*-
import logging
from datetime import datetime

from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.black_fennec.structure.type.type_factory import TypeFactory

logger = logging.getLogger(__name__)


def create_date_time_range_type():
    """DateTimeRange Type
    Defines the format of the date time range
    """
    tf = TypeFactory()
    iso_regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-' \
                r'(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):' \
                r'([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):' \
                r'[0-5][0-9])?$'

    type = tf.create_map(properties={
        DateTimeRange.START_KEY: tf.create_string(pattern=iso_regex),
        DateTimeRange.END_KEY: tf.create_string(pattern=iso_regex)
    })

    return type


class DateTimeRange:
    """DateTimeRange Base Type"""
    TYPE = None
    START_KEY = 'date_time_start'
    END_KEY = 'date_time_end'

    def __init__(self, subject: Map = None):
        """DateTimeRange Constructor

        Args:
            subject (Map): underlying map interpretation to
                which property calls are dispatched
        """
        self._subject: Map = subject or Map()
        if DateTimeRange.START_KEY not in self.subject.value:
            default_start_time: datetime = datetime.min
            self.subject.add_item(
                DateTimeRange.START_KEY,
                String(default_start_time.isoformat())
            )

        if DateTimeRange.END_KEY not in self.subject.value:
            default_end_time: datetime = datetime.max
            self.subject.add_item(
                DateTimeRange.END_KEY,
                String(default_end_time.isoformat())
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
    def date_time_start(self) -> datetime:
        """start getter

        Raises:
            ValueError: if the value contained in the underlying map
                could not have been parsed. Expects iso format.
        """
        date_time_start_string = self._get_value(DateTimeRange.START_KEY)
        try:
            value: datetime = \
                datetime.fromisoformat(date_time_start_string)
        except ValueError:
            logger.error('could not parse start date time format')
            value: datetime = datetime.min
        return value

    @date_time_start.setter
    def date_time_start(self, value: datetime):
        self._set_value(DateTimeRange.START_KEY, value.isoformat())

    @property
    def date_time_end(self) -> datetime:
        date_time_end_string = self._get_value(DateTimeRange.END_KEY)
        try:
            value: datetime = datetime.fromisoformat(date_time_end_string)
        except ValueError:
            logger.error('could not parse end date time format')
            value: datetime = datetime.max
        return value

    @date_time_end.setter
    def date_time_end(self, value: datetime):
        self._set_value(DateTimeRange.END_KEY, value.isoformat())


DateTimeRange.TYPE = create_date_time_range_type()
