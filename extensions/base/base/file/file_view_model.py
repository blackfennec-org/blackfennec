# -*- coding: utf-8 -*-
import logging

from blackfennec.interpretation.interpretation import Interpretation
from blackfennec.document_system.document_registry import DocumentRegistry
from blackfennec.util.change_notification_dispatch_mixin import ChangeNotificationDispatchMixin

from base.file.file import File

logger = logging.getLogger(__name__)


class FileViewModel(ChangeNotificationDispatchMixin):
    """View model for core type File."""

    def __init__(self,
            interpretation: Interpretation, 
            document_registry: DocumentRegistry):
        super().__init__()

        self._interpretation = interpretation
        self._document_registry = document_registry
        self._model: File = File(interpretation.structure)
        self._model.bind(changed=self._dispatch_change_notification)

    @property
    def file_path(self):
        """Property for file path"""
        return self._model.file_path

    @file_path.setter
    def file_path(self, value: str):
        self._model.file_path = value

    @property
    def absolute_path(self):
        if self.file_path.startswith('/'):
            return self.file_path
        absolute_path = f'{self.location}/{self.file_path}'
        return absolute_path

    @absolute_path.setter
    def absolute_path(self, value: str):
        relative_path = value.replace(f'{self.location}/', '')
        self.file_path = relative_path

    @property
    def file_type(self):
        """Property for file type"""
        return self._model.file_type

    @file_type.setter
    def file_type(self, value: str):
        self._model.file_type = value

    @property
    def location(self):
        structure = self._interpretation.structure
        document = self._document_registry.get_document(structure)
        return document.location

    def navigate(self):
        self._interpretation.navigate(self._interpretation.structure)
