# -*- coding: utf-8 -*-
import logging

from blackfennec.interpretation.interpretation import Interpretation
from blackfennec.util.change_notification_dispatch_mixin import ChangeNotificationDispatchMixin
from blackfennec.structure.map import Map

from base.file.file import File

logger = logging.getLogger(__name__)


class FileViewModel(ChangeNotificationDispatchMixin):
    """View model for core type File."""

    def __init__(self, interpretation: Interpretation):
        """Create constructor

        Args:
            interpretation (Interpretation): The overarching
                interpretation
        """
        super().__init__()

        self._interpretation = interpretation
        self._model: File = File(interpretation.structure)
        self._model.bind(changed=self._dispatch_change_notification)

    @property
    def file_path(self):
        """Property for file path"""
        return self._model.file_path

    @file_path.setter
    def file_path(self, value: str):
        logger.debug('File_path setter with string called')
        self._model.file_path = value

    @property
    def file_type(self):
        """Property for file type"""
        return self._model.file_type

    @file_type.setter
    def file_type(self, value: str):
        self._model.file_type = value

    def navigate(self):
        self._interpretation.navigate(self._interpretation.structure)
