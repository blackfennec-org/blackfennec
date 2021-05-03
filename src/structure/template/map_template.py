# -*- coding: utf-8 -*-
from src.structure.map import Map
from src.structure.template.template_base import TemplateBase


class MapTemplate(TemplateBase, Map):
    def __init__(self, subject: Map, template_factory, property_storage: dict = None):
        TemplateBase.__init__(self, subject, template_factory, property_storage)

    @property
    def subject(self) -> Map:
        return self._subject

    @property
    def children(self):
        result = list()
        if not self.subject.children:
            return result
        for child in self.subject.children:
            result.append(self._template_factory.create(child, self._property_storage))
        return result

    def __getitem__(self, key):
        item = self.subject[key]
        return self._template_factory.create(item, self._property_storage)

    def __setitem__(self, key, value):
        decapsulated_value = value
        if isinstance(value, TemplateBase):
            base: TemplateBase = value
            decapsulated_value = base.subject
        self.subject[key] = decapsulated_value
        decapsulated_value.parent = self.subject

    def __repr__(self):
        return f'MapTemplate({self.subject.__repr__()})'