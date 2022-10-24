# -*- coding: utf-8 -*-
import logging

from blackfennec.structure.map import Map
from blackfennec.structure.string import String

logger = logging.getLogger(__name__)


class File:
    """File BaseType Class

    Helper class used by the file view_model representing
    the actual type 'File'.
    Can be used by other classes as a helper to be able to
    include files in a overlaying datatype.
    """
    TYPE = None
    FILE_PATH_KEY = 'file_path'
    FILE_TYPE_KEY = 'file_type'

    def __init__(self, subject: Map = None):
        """File Constructor

        Args:
            subject (Map): underlying map interpretation to
                which property calls are dispatched
        """
        self._subject: Map = subject or Map()
        if File.FILE_PATH_KEY not in self._subject.value:
            self._subject.add_item(File.FILE_PATH_KEY, String())
        if File.FILE_TYPE_KEY not in self._subject.value:
            self._subject.add_item(File.FILE_TYPE_KEY, String())

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
    def file_path(self) -> str:
        return self._get_value(File.FILE_PATH_KEY)

    @file_path.setter
    def file_path(self, value: str):
        self._set_value(File.FILE_PATH_KEY, value)

    @property
    def file_type(self) -> str:
        return self._get_value(File.FILE_TYPE_KEY)

    @file_type.setter
    def file_type(self, value: str):
        self._set_value(File.FILE_TYPE_KEY, value)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f'File({self.file_path}, {self.file_type})'
