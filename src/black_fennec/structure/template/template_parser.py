# -*- coding: utf-8 -*-
from src.black_fennec.util.parameterized_visitor import ParameterizedVisitor
from src.black_fennec.structure.map import Map

from .template import Template
from .list_template import ListTemplate
from .map_template import MapTemplate
from .string_template import StringTemplate
from .number_template import NumberTemplate


class TemplateParser(ParameterizedVisitor):
    """Template Parser

    Class is a concrete factory which produces Template based
        structure encapsulations. Only few methods are overwritten
        which require specialised functionality. For all other
        structure types the abstract factory implementation suffices.
    """

    def __init__(self):
        ParameterizedVisitor.__init__(
            self, default=self.assertion_error, map=self.parse
        )

    def parse(self, template_map: Map) -> Template:
        factory_map = {
            "Map": MapTemplate,
            "List": ListTemplate,
            "String": StringTemplate,
            "Number": NumberTemplate,
        }
        type_name = template_map.value["type"].value
        create_template = factory_map[type_name]
        return create_template(self, template_map)

    def assertion_error(self, subject):
        assert False, f"You try to interpret {subject} type as template"
