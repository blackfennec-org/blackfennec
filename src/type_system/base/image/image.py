# -*- coding: utf-8 -*-
import logging

from src.structure.map import Map
from src.structure.root import Root
from src.structure.string import String
from src.structure.template.template_factory_visitor import TemplateFactoryVisitor
from src.type_system.base.file.file import File

logger = logging.getLogger(__name__)


def create_image_template():
    """File Template
    Defines the format of the file
    """
    template_map = Map()
    template_map[File.FILE_PATH_KEY] = String()
    template_map[File.FILE_TYPE_KEY] = String('image/')

    template_factory = TemplateFactoryVisitor()
    template = template_map.accept(template_factory)
    return template


class Image(File):
    """Image BaseType Class

    Helper class used by the image view_model representing
    the actual type 'Image'.
    Can be used by other classes as a helper to be able to
    include images in a overlaying datatype.
    """

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


Image.TEMPLATE = create_image_template()
