# -*- coding: utf-8 -*-

from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.template.list_template import ListTemplate
from src.black_fennec.structure.template.map_template import MapTemplate
from src.black_fennec.structure.template.string_template import StringTemplate
from src.black_fennec.structure.template.number_template import NumberTemplate
from .template_parser import TemplateParser


class TemplateFactory:
    def create_map(self, properties=None):
        template = MapTemplate(
            TemplateParser(),
            Map({"type": String("Map"), "required": List(), "properties": Map()}),
        )

        if properties:
            for name, value in properties.items():
                template.add_property(name, value)

        return template

    def create_list(self):
        template = ListTemplate(
            TemplateParser(),
            Map({
                "type": String("List"), 
                "elements": List()
            })
        )
        return template

    def create_string(self, pattern=".*", default=""):
        return StringTemplate(
            TemplateParser(),
            Map(
                {
                    "type": String("String"),
                    "pattern": String(pattern),
                    "default": String(default),
                }
            ),
        )

    def create_number(self, min=None, max=None, default=0):
        return NumberTemplate(
            TemplateParser(),
            Map({"type": String("Number"), "default": Number(default)}),
        )
