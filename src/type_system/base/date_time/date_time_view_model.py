# -*- coding: utf-8 -*-
import logging
from datetime import datetime

from src.type_system.base.date_time.date_time import DateTime
from src.interpretation.interpretation import Interpretation

logger = logging.getLogger(__name__)


class DateTimeViewModel:
    """View model for core type DateTime."""

    def __init__(self, interpretation: Interpretation):
        """Create constructor

        Args:
            interpretation (Interpretation): The overarching
                interpretation
        """
        self._model: DateTime = DateTime(interpretation.info)

    @property
    def date_time(self) -> datetime:
        """Property for first name"""
        return self._model.date_time

    @date_time.setter
    def date_time(self, value: datetime):
        self._model.date_time = value
