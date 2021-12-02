# -*- coding: utf-8 -*-
import logging

from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.black_fennec.structure.template.template_factory_visitor import TemplateFactoryVisitor
from src.visualisation.base.file.file import File

logger = logging.getLogger(__name__)


def create_image_template():
    """File Template
    Defines the format of the file
    """
    template_map = Map({
        File.FILE_PATH_KEY: String(),
        File.FILE_TYPE_KEY: String('image/')
    })

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

    def __init__(self, subject: Map = Map()):
        """Image Constructor

        Args:
            subject (Map): underlying map interpretation to
                which property calls are dispatched
        """
        if File.FILE_TYPE_KEY not in subject.value:
            subject.add_item(File.FILE_TYPE_KEY, String('image/unknown'))
        File.__init__(self, subject)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f'Image({self.file_path}, {self.file_type})'


Image.TEMPLATE = create_image_template()
