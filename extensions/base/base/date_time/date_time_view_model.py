# -*- coding: utf-8 -*-
import logging
from datetime import datetime

from blackfennec.util.change_notification_dispatch_mixin import \
    ChangeNotificationDispatchMixin
from blackfennec.util.observable import Observable
from base.date_time.date_time import DateTime
from blackfennec.interpretation.interpretation import Interpretation

logger = logging.getLogger(__name__)


class DateTimeViewModel(ChangeNotificationDispatchMixin):
    """View model for core type DateTime."""

    def __init__(self, interpretation: Interpretation):
        """Create constructor

        Args:
            interpretation (Interpretation): The overarching
                interpretation
        """
        super().__init__()

        self._interpretation = interpretation
        self._model: DateTime = DateTime(interpretation.structure)
        self._model.bind(changed=self._dispatch_change_notification)

    @property
    def date_time(self) -> datetime:
        return self._model.date_time

    @date_time.setter
    def date_time(self, value: datetime):
        self._model.date_time = value

    def navigate(self):
        self._interpretation.navigate(self._interpretation.structure)
