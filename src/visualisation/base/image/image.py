# -*- coding: utf-8 -*-
import logging

from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.black_fennec.structure.type.type_factory import TypeFactory
from src.visualisation.base.file.file import File, create_file_type

logger = logging.getLogger(__name__)


def create_image_type():
    """File Type
    Defines the format of the file
    """
    tf = TypeFactory()
    type = tf.create_map(type="Image", super=create_file_type(), properties={
        File.FILE_PATH_KEY: tf.create_string(),
        File.FILE_TYPE_KEY: tf.create_string('^image/.*$')
    })

    return type


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


Image.TYPE = create_image_type()
