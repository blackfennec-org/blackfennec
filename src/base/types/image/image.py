# -*- coding: utf-8 -*-
import logging

from src.base.types.file.file import File
from src.core.map import Map
from src.core.string import String

logger = logging.getLogger(__name__)


class Image(File):
    FILE_PATH_KEY = 'file_path'
    FILE_TYPE_KEY = 'file_type'

    def __init__(self, map_interpretation: Map = Map()):
        """Image Constructor

        Args:
            map_interpretation (Map): underlying map interpretation to
                which property calls are dispatched
        """
        if Image.FILE_TYPE_KEY not in map_interpretation:
            map_interpretation[Image.FILE_TYPE_KEY] = String('image/unknown')
        super().__init__(map_interpretation)
        self._data: Map = map_interpretation

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return 'Image({}, {})'.format(
            self.file_path,
            self.file_type
        )
