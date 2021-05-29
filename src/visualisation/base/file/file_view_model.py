# -*- coding: utf-8 -*-
import logging

from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.structure.map import Map
from src.visualisation.base.file.file import File

logger = logging.getLogger(__name__)


class FileViewModel:
    """View model for core type File."""

    def __init__(self, interpretation: Interpretation):
        """Create constructor

        Args:
            interpretation (Interpretation): The overarching
                interpretation
        """
        if not isinstance(interpretation.info, Map):
            message = 'interpretation received should be of' \
                      ' super type Map, but is of type %s'
            logger.warning(message, type(interpretation.info))
        self._model: File = File(interpretation.info)
        self._interpretation = interpretation

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
        self._interpretation.navigate(self._interpretation.info)
