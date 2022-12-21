# -*- coding: utf-8 -*-

from blackfennec.layers.encapsulation_base.encapsulation_base import EncapsulationBase
from blackfennec.structure.structure import Structure


class ObservableBase(EncapsulationBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._subject.bind(changed=self._layer.on_changed)

    @staticmethod
    def _decapsulate(item: Structure):
        decapsulated_value = item
        if isinstance(item, ObservableBase):
            factory_base: ObservableBase = item
            decapsulated_value = factory_base.subject
        return decapsulated_value
