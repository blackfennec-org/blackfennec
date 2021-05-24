# -*- coding: utf-8 -*-
from collections import UserDict

from src.black_fennec.structure.encapsulation_base.encapsulation_base import EncapsulationBase
from src.black_fennec.structure.info import Info
from src.black_fennec.structure.map import Map


class MapEncapsulationBase(EncapsulationBase, Map):
    """Base Class for Encapsulation of a Map."""
    def __init__(
            self,
            visitor: 'BaseFactoryVisitor',
            subject: Map,
    ):
        UserDict.__init__(self)
        EncapsulationBase.__init__(
            self,
            visitor,
            subject
        )

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
            key: self._remove_encapsulation(item)
            for key, item in value.items()
        }

    def __getitem__(self, key):
        item: Info = self.subject[key]
        return item.accept(self._visitor)

    def __setitem__(self, key, value: Info):
        decapsulated_value = self._remove_encapsulation(value)
        self.subject[key] = decapsulated_value
        decapsulated_value.parent = self.subject

    def __repr__(self):
        return f'MapEncapsulationBase({self.subject.__repr__()})'
