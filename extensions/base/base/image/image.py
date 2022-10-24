# -*- coding: utf-8 -*-
import logging

from blackfennec.structure.map import Map
from blackfennec.structure.string import String
from base.file.file import File

logger = logging.getLogger(__name__)


class Image(File):
    """Image BaseType Class

    Helper class used by the image view_model representing
    the actual type 'Image'.
    Can be used by other classes as a helper to be able to
    include images in a overlaying datatype.
    """

    def __init__(self, subject: Map = None):
        """Image Constructor

        Args:
            subject (Map): underlying map interpretation to
                which property calls are dispatched
        """
        subject = subject or Map()
        if File.FILE_TYPE_KEY not in subject.value:
            subject.add_item(File.FILE_TYPE_KEY, String('image/unknown'))
        File.__init__(self, subject)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f'Image({self.file_path}, {self.file_type})'

