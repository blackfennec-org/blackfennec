from typing import Optional
from blackfennec.structure.visitor import Visitor
from blackfennec.structure.structure import Structure
import blackfennec.structure.merge.deep_merge as deep_merge
from blackfennec.structure.merge.merged_phantom import MergedPhantom
from blackfennec.util.intercepting_visitor import InterceptingVisitor

import logging

logger = logging.getLogger(__name__)


class MergedStructure(Structure):
    def __init__(self, underlay: Structure, overlay: Structure):
        super().__init__()
        assert underlay is not None, "Underlay cannot be None"
        assert overlay is not None, "Overlay cannot be None"
        self._underlay = underlay
        self._overlay = overlay

    @property
    def subject(self):
        if self._overlay.value is not None:
            return self._overlay
        return self._underlay

    def accept(self, visitor: Visitor):
        interceptor = InterceptingVisitor(lambda s: self, visitor)
        return self.subject.accept(interceptor)

    @property
    def value(self):
        return self.subject.value

    @value.setter
    def value(self, value):
        raise AssertionError("Value cannot be set on MergedStructure")

    def _parent_or_phantom(self, left, right):
        if left.parent:
            return left.parent
        else:
            return MergedPhantom(None, right.parent)

    @property
    def parent(self) -> Optional['MergedStructure']:
        underlay_parent = self._parent_or_phantom(self._underlay, self._overlay)
        overlay_parent = self._parent_or_phantom(self._overlay, self._underlay)

        if underlay_parent or overlay_parent:
            return self._encapsulate(underlay_parent, overlay_parent)

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

    def _encapsulate(self, underlay: Structure, overlay: Structure) -> 'MergedStructure':
        return deep_merge.DeepMerge.merge(underlay, overlay)

    def __repr__(self) -> str:
        return f"MergedStructure(underlay={self._underlay}, overlay={self._overlay})"
