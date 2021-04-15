# -*- coding: utf-8 -*-
import logging

from src.base.types.image.image import Image
from src.core import Interpretation
from src.core.map import Map
from src.core.string import String

logger = logging.getLogger(__name__)


class ImageViewModel:
    """View model for core type Image."""

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
        self._model: Image = Image(interpretation.info)

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
