# -*- coding: utf-8 -*-
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.list import List
from src.black_fennec.structure.template.map_template import MapTemplate as Template
from src.black_fennec.structure.template.template_parser import TemplateParser


class MapTemplate(Template):
    """Template of map.

    Class creates Template structure for core type
        map."""

    def __init__(self):
        visitor = TemplateParser()
        Template.__init__(self, visitor, Map(
            {'required': List(), 'properties': Map()}))

        self._name = 'Map'

    @property
    def name(self):
        return self._name
