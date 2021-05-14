# -*- coding: utf-8 -*-
import logging
from datetime import datetime


from src.interpretation.interpretation import Interpretation
from src.type_system.base.date_time_range.date_time_range import DateTimeRange

logger = logging.getLogger(__name__)


class DateTimeRangeViewModel:
    """View model for core type DateTimeRange."""

    def __init__(self, interpretation: Interpretation):
        """Create constructor

        Args:
            interpretation (Interpretation): The overarching
                interpretation
        """
        self._model: DateTimeRange = DateTimeRange(interpretation.info)

    @property
    def date_time_start(self) -> datetime:
        """Property for start date"""
        return self._model.date_time_start

    @date_time_start.setter
    def date_time_start(self, value: datetime):
        self._model.date_time_start = value

    @property
    def date_time_end(self) -> datetime:
        """Property for end date"""
        return self._model.date_time_end

    @date_time_end.setter
    def date_time_end(self, value: datetime):
        self._model.date_time_end = value

