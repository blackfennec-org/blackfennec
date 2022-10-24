# -*- coding: utf-8 -*-
import logging

from blackfennec.structure.type.type import Type
from blackfennec.type_system.type_registry import TypeRegistry
from base.image.image import Image
from blackfennec.interpretation.interpretation import Interpretation
from blackfennec.structure.map import Map

logger = logging.getLogger(__name__)


class ImageViewModel:
    """View model for core type Image."""

    def __init__(self, interpretation: Interpretation):
        """Create constructor

        Args:
            interpretation (Interpretation): The overarching
                interpretation
        """
        if not isinstance(interpretation.structure, Map):
            message = 'interpretation received should be of' \
                      ' super type Map, but is of type %s'
            logger.warning(message, type(interpretation.structure))
        self._interpretation = interpretation
        self._model: Image = Image(interpretation.structure)

    @property
    def file_path(self):
        """Property for image path"""
        return self._model.file_path

    @file_path.setter
    def file_path(self, value: str):
        logger.debug('Image_path setter with string called')
        self._model.file_path = value

    @property
    def file_type(self):
        """Property for image type"""
        return self._model.file_type

    @file_type.setter
    def file_type(self, value: str):
        self._model.file_type = value

    def navigate(self):
        self._interpretation.navigate(self._interpretation.structure)
