# -*- coding: utf-8 -*-
import logging

from src.structure.map import Map
from src.structure.string import String

logger = logging.getLogger(__name__)


class File:
    FILE_PATH_KEY = 'file_path'
    FILE_TYPE_KEY = 'file_type'

    def __init__(self, map_interpretation: Map = Map()):
        """File Constructor

        Args:
            map_interpretation (Map): underlying map interpretation to
                which property calls are dispatched
        """
        self._data: Map = map_interpretation
        if File.FILE_PATH_KEY not in self._data:
            self._data[File.FILE_PATH_KEY] = String()
        if File.FILE_TYPE_KEY not in self._data:
            self._data[File.FILE_TYPE_KEY] = String()

    def _get_from_map(self, key) -> str:
        """Wrapper for map access

        Checks whether key is in map and if yes, it
        returns its value. Otherwise None is returned.

        Args:
            key (str): Key of value to check

        Returns:
            : Value at key in map
        """
        if key not in self._data:
            return None
        return self._data[key].value

    @property
    def file_path(self) -> str:
        return self._get_from_map(File.FILE_PATH_KEY)

    @file_path.setter
    def file_path(self, value: str):
        self._data[File.FILE_PATH_KEY].value = value

    @property
    def file_type(self) -> str:
        return self._get_from_map(File.FILE_TYPE_KEY)

    @file_type.setter
    def file_type(self, value: str):
        self._data[File.FILE_TYPE_KEY].value = value

    def __eq__(self, other) -> bool:
        return (
                   self.file_path,
                   self.file_type
               ) == (
                   other.file_path,
                   other.file_type
               )

    def __ne__(self, other) -> bool:
        return not self == other

    def __str__(self) -> str:
        """Convert to string"""
        return str(self.file_path) + ' (' + \
               str(self.file_type) + ')'

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return 'File({}, {})'.format(
            self.file_path,
            self.file_type
        )
