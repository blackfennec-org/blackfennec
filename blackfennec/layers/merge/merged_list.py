from blackfennec.structure.structure import Structure
import blackfennec.layers.merge.deep_merge as deep_merge
from .merged_structure import MergedStructure
from .merged_phantom import MergedPhantom

import logging

logger = logging.getLogger(__name__)


class MergedList(MergedStructure):
    def __init__(self, underlay: Structure, overlay: Structure):
        super().__init__(underlay, overlay)

    def _value_or_empty(self, structure):
        if structure.value is None:
            return []
        return structure.value

    @property
    def value(self):
        logger.info("Accessed value of merged list: implementation is disputed")
        underlay = self._value_or_empty(self._underlay)
        overlay = self._value_or_empty(self._overlay)
        value = underlay + overlay
        return [
            self._encapsulate(MergedPhantom(self, child), child)
            for child in value
        ]

    @value.setter
    def value(self, value):
        raise AssertionError("Cannot set value on merged layer")

    def __repr__(self) -> str:
        return f"MergedList(underlay={self._underlay}, overlay={self._overlay})"
