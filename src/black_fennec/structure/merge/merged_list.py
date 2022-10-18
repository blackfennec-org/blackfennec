from src.black_fennec.structure.structure import Structure
import src.black_fennec.structure.merge.deep_merge as deep_merge
from .merged_structure import MergedStructure
from .merged_phantom import MergedPhantom

import logging

logger = logging.getLogger(__name__)

class MergedList(MergedStructure):
    def __init__(self, underlay: Structure, overlay: Structure):
        super().__init__(underlay, overlay)
        logger.info("MergedList is not implemented")

    @property
    def value(self):
        logger.warning("Accessed value of merged list: implementation is disputed")
        underlay = self._underlay.value if self._underlay else []
        overlay = self._overlay.value if self._overlay else []
        value = underlay + overlay
        return [
            deep_merge.DeepMerge.merge(MergedPhantom(self, child), child)
            for child in value
        ]

    @value.setter
    def value(self, value):
        raise AssertionError("Cannot set value on merged layer")

    def __repr__(self) -> str:
        return f"MergedList(underlay={self._underlay}, overlay={self._overlay})"
