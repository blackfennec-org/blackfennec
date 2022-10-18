from src.black_fennec.structure.structure import Structure
import src.black_fennec.structure.merge.deep_merge as deep_merge
from .merged_structure import MergedStructure
from .merged_phantom import MergedPhantom

import logging

logger = logging.getLogger(__name__)

class MergedMap(MergedStructure):
    def __init__(self, underlay: Structure, overlay: Structure):
        super().__init__(underlay, overlay)

    @property
    def value(self):
        result = {}
        underlay = self._underlay.value if self._underlay else {}
        overlay = self._overlay.value if self._overlay else {}
        for key, value in underlay.items():
            if key in overlay:
                result[key] = deep_merge.DeepMerge.merge(value, overlay[key])
            else:
                result[key] = deep_merge.DeepMerge.merge(
                    value, MergedPhantom(self._overlay, value)
                )
        for key, value in overlay.items():
            if key not in underlay:
                result[key] = deep_merge.DeepMerge.merge(
                    MergedPhantom(self._underlay, value), value
                )
        return result

    @value.setter
    def value(self, value):
        raise AssertionError("Cannot set value on merged layer")

    def __repr__(self) -> str:
        return f"MergedMap(underlay={self._underlay}, overlay={self._overlay})"
