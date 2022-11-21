from blackfennec.structure.null import Null
from blackfennec.structure.visitor import Visitor
from blackfennec.structure.structure import Structure
from .merged_structure import MergedStructure

import logging

logger = logging.getLogger(__name__)


class MergedNull(MergedStructure):
    def __init__(self, layer, underlay: Structure, overlay: Structure):
        assert isinstance(underlay.structure, Null), f"underlay must be a Null, not {underlay.structure}"
        assert isinstance(overlay.structure, Null), f"overlay must be a Null, not {overlay.structure}"
        super().__init__(layer, underlay, overlay)

    @property
    def value(self):
        return None

    @value.setter
    def value(self, value):
        raise AssertionError("Value cannot be set on MergedStructure")

    def accept(self, visitor: Visitor):
        return visitor.visit_null(self)

    def __repr__(self) -> str:
        return f"MergedNull()"
