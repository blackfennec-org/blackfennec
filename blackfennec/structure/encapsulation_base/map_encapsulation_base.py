# -*- coding: utf-8 -*-

from blackfennec.structure.encapsulation_base.encapsulation_base import EncapsulationBase
from blackfennec.structure.map import Map
from blackfennec.structure.structure import Structure


class MapEncapsulationBase(EncapsulationBase, Map):
    """Base Class for Encapsulation of a Map."""

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
        Map.__init__(self)

    @property
    def subject(self) -> Map:
        return self._subject

    @property
    def value(self):
        return {
            key: item.accept(self._visitor)
            for key, item in self.subject.value.items()
        }

    @value.setter
    def value(self, value):
        self.subject.value = {
            key: self._decapsulate(item)
            for key, item in value.items()
        }

    def remove_item(self, key):
        self.subject.remove_item(key)

    def add_item(self, key, value: Structure):
        decapsulated_value = self._decapsulate(value)
        self.subject.add_item(key, decapsulated_value)
        decapsulated_value.parent = self.subject

    def __repr__(self):
        return f'MapEncapsulationBase({self.subject.__repr__()})'