# -*- coding: utf-8 -*-
import logging

from src.visualisation.base.image.image import Image
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.structure.map import Map

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
