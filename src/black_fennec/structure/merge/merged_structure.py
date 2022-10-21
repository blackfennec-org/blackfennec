from multiprocessing import parent_process
from typing import Optional
from src.black_fennec.structure.visitor import Visitor
from src.black_fennec.structure.structure import Structure
import src.black_fennec.structure.merge.deep_merge as deep_merge
from src.black_fennec.util.intercepting_visitor import InterceptingVisitor
from .merged_phantom import MergedPhantom

import logging

logger = logging.getLogger(__name__)


class MergedStructure(Structure):
    def __init__(self, underlay: Structure, overlay: Structure):
        super().__init__()
        self._underlay = underlay
        self._overlay = overlay

    @property
    def subject(self):
        return self._overlay or self._underlay

    def accept(self, visitor: Visitor):
        interceptor = InterceptingVisitor(lambda s: self, visitor)
        return self._underlay.accept(interceptor)

    @property
    def value(self):
        return self.subject.value

    @value.setter
    def value(self, value):
        raise AssertionError("Value cannot be set on MergedStructure")

    @property
    def parent(self) -> Optional['MergedStructure']:
        if self._overlay.parent:
            overlay_parent = self._overlay.parent
        else:
            if self._underlay.parent:
                underlay_parent = self._underlay.parent
            else:
                underlay_parent = None
            overlay_parent = MergedPhantom(None, underlay_parent)

        if self._underlay.parent:
            underlay_parent = self._underlay.parent
        else:
            if self._overlay.parent:
                overlay_parent = self._overlay.parent
            else:
                overlay_parent = None
            underlay_parent = MergedPhantom(None, overlay_parent)

        if underlay_parent or overlay_parent:
            return deep_merge.DeepMerge.merge(underlay_parent, overlay_parent)

        return None

    @parent.setter
    def parent(self, parent: Structure):
        raise AssertionError("Cannot set parent on MergedStructure")

    @property
    def structure(self) -> Structure:
        return self.subject.structure

    def get_root(self) -> Optional["MergedStructure"]:
        parent = self.parent
        if parent:
            return parent.get_root()
        return None

    def __repr__(self) -> str:
        return f"MergedStructure(underlay={self._underlay}, overlay={self._overlay})"
