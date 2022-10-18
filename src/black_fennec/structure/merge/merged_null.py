from src.black_fennec.structure.visitor import Visitor
from src.black_fennec.structure.structure import Structure
from src.black_fennec.util.intercepting_visitor import InterceptingVisitor
from .merged_structure import MergedStructure


import logging

logger = logging.getLogger(__name__)

class MergedNull(MergedStructure):
    def __init__(self, underlay: Structure, overlay: Structure):
        super().__init__(underlay, overlay)

    @property
    def _layer(self):
        if self._overlay and self._overlay.value is not None:
            return self._overlay
        return self._underlay

    @property
    def value(self):
        return self._layer.value

    @value.setter
    def value(self, value):
        raise AssertionError("Value cannot be set on MergedStructure")

    def accept(self, visitor: Visitor):
        interceptor = InterceptingVisitor(lambda s: self, visitor)
        return self._layer.accept(interceptor)

    def __repr__(self) -> str:
        return f"MergedNull(underlay={self._underlay}, overlay={self._overlay})"

