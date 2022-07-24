# -*- coding: utf-8 -*-

from src.black_fennec.structure.encapsulation_base.base_factory_visitor import BaseFactoryVisitor
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.template.list_template import ListTemplate
from src.black_fennec.structure.template.map_template import MapTemplate
from src.black_fennec.structure.template.string_template import StringTemplate
from src.black_fennec.structure.template.number_template import NumberTemplate
from src.black_fennec.structure.template.template_base import TemplateBase


class TemplateFactoryVisitor(BaseFactoryVisitor):
    '''Template Factory Visitor

    Class is a concrete factory which produces Template based
        structure encapsulations. Only few methods are overwritten
        which require specialised functionality. For all other
        structure types the abstract factory implementation suffices.
    '''

    def __init__(self):
        BaseFactoryVisitor.__init__(self, TemplateBase)

    def create_template(
            self, template_map: Map,
            is_optional: bool = False) -> TemplateBase:
        factory_map = {
            'Map': MapTemplate,
            'String': StringTemplate,
            'Number': NumberTemplate
        }
        type_name = template_map.value['type'].value
        create_template = factory_map[type_name]
        return create_template(self, template_map, is_optional)

    def create_map(self, properties=None, is_optional=False):
        template = MapTemplate(self, Map({
            'type': String('Map'),
            'required': List(),
            'properties': Map()
        }), is_optional)

        if properties:
            for name, value in properties.items():
                template.add_property(name, value)

        return template

    def create_string(self, pattern='.*', default='', is_optional=False):
        return StringTemplate(self, Map({
            'type': String('String'),
            'pattern': String(pattern),
            'default': String(default)
        }), is_optional)

    def create_number(self, min=None, max=None, default=0, is_optional=False):
        return NumberTemplate(self, Map({
            'type': String('Number'),
            'default': Number(default)
        }), is_optional)

    def visit_string(self, subject_string: String) -> StringTemplate:
        return StringTemplate(self, subject_string)

    def visit_map(self, subject_map: Map) -> MapTemplate:
        return MapTemplate(self, subject_map)

    def visit_list(self, subject_list: List) -> ListTemplate:
        return ListTemplate(self, subject_list)
