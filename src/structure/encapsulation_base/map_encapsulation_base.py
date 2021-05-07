# -*- coding: utf-8 -*-
from src.structure.encapsulation_base.encapsulation_base import EncapsulationBase
from src.structure.info import Info
from src.structure.map import Map


class MapEncapsulationBase(EncapsulationBase, Map):
    def __init__(
            self,
            visitor: 'BaseFactoryVisitor',
            subject: Map,
    ):
        EncapsulationBase.__init__(
            self,
            visitor,
            subject
        )

    @property
    def subject(self) -> Map:
        return self._subject

    def __getitem__(self, key):
        item: Info = self.subject[key]
        return item.accept(self._visitor)

    def __setitem__(self, key, value: Info):
        decapsulated_value = self._remove_template_class(value)
        self.subject[key] = decapsulated_value
        decapsulated_value.parent = self.subject

    def __repr__(self):
        return f'MapEncapsulationBase({self.subject.__repr__()})'