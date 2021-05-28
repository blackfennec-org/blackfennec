# -*- coding: utf-8 -*-
import logging
from datetime import datetime

from src.black_fennec.structure.info import Info

from src.visualisation.base.date_time.date_time import DateTime
from src.black_fennec.interpretation.interpretation import Interpretation

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
        self._interpretation = interpretation

    @property
    def date_time(self) -> datetime:
        """Property for first name"""
        return self._model.date_time

    @date_time.setter
    def date_time(self, value: datetime):
        self._model.date_time = value

    def navigate(self):
        self._interpretation.navigate(self._interpretation.info)
