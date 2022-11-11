from blackfennec.structure.structure import Structure
import blackfennec.layers.merge.deep_merge as deep_merge
from .merged_structure import MergedStructure
from .merged_phantom import MergedPhantom

import logging

logger = logging.getLogger(__name__)


class MergedMap(MergedStructure):
    def __init__(self, underlay: Structure, overlay: Structure):
        super().__init__(underlay, overlay)

    def _value_or_empty(self, structure):
        if structure.value is None:
            return {}
        return structure.value

    @property
    def value(self):
        result = {}
        underlay = self._value_or_empty(self._underlay)
        overlay = self._value_or_empty(self._overlay)
        for key, value in underlay.items():
            if key in overlay:
                result[key] = self._encapsulate(value, overlay[key])
            else:
                result[key] = self._encapsulate(
                    value, MergedPhantom(self._overlay, value)
                )
        for key, value in overlay.items():
            if key not in underlay:
                result[key] = self._encapsulate(
                    MergedPhantom(self._underlay, value), value
                )
        return result

    @value.setter
    def value(self, value):
        raise AssertionError("Cannot set value on merged layer")

    def __repr__(self) -> str:
        return f"MergedMap(underlay={self._underlay}, overlay={self._overlay})"
