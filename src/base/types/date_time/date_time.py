# -*- coding: utf-8 -*-
import logging

from src.core.types.map import Map
from src.core.types.string import String
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class DateTime:
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
