from src.black_fennec.structure.visitor import Visitor
from src.black_fennec.structure.structure import Structure
import src.black_fennec.structure.merge.deep_merge as deep_merge
from src.black_fennec.util.intercepting_visitor import InterceptingVisitor

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
        subject = self._overlay or self._underlay
        return subject.value

    @value.setter
    def value(self, value):
        raise AssertionError("Value cannot be set on MergedStructure")

    @property
    def parent(self):
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

    @parent.setter
    def parent(self, parent: Structure):
        raise AssertionError("Cannot set parent on MergedStructure")

    def get_root(self):
        return deep_merge.DeepMerge.merge(self._underlay.get_root(), self._overlay.get_root())

    @property
    def structure(self):
        return self.subject.structure

    def __repr__(self) -> str:
        return f"MergedStructure(underlay={self._underlay}, overlay={self._overlay})"


class MergedList(MergedStructure):
    def __init__(self, underlay: Structure, overlay: Structure):
        super().__init__(underlay, overlay)
        logger.info("MergedList is not implemented")

    @property
    def value(self):
        logger.info("Accessed value of merged list: implementation is disputed")
        underlay = self._underlay.value if self._underlay else []
        overlay = self._overlay.value if self._overlay else []
        value = underlay + overlay
        return [deep_merge.DeepMerge.merge(MergedPhantom(self, child), child)
                for child in value]

    @value.setter
    def value(self, value):
        raise AssertionError("Cannot set value on merged layer")

    def __repr__(self) -> str:
        return f"MergedList(underlay={self._underlay}, overlay={self._overlay})"


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
                result[key] = deep_merge.DeepMerge.merge(value, MergedPhantom(self._overlay, value))
        for key, value in overlay.items():
            if key not in underlay:
                result[key] = deep_merge.DeepMerge.merge(MergedPhantom(self._underlay, value), value)
        return result

    @value.setter
    def value(self, value):
        raise AssertionError("Cannot set value on merged layer")

    def __repr__(self) -> str:
        return f"MergedMap(underlay={self._underlay}, overlay={self._overlay})"


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


class MergedPhantom:
    """A mock object to allow navigating a phantom structure for merging"""

    def __init__(self, parent, twin):
        self._parent = parent
        self._twin = twin

    @property
    def parent(self):
        return self._parent

    @property
    def value(self):
        return None

    def accept(self, visitor):
        interceptor = InterceptingVisitor(lambda s: self, visitor)
        return self._twin.accept(interceptor)

    def __bool__(self):
        return False

    def __repr__(self) -> str:
        return f"MergedPhantom(parent={self._parent}, twin={self._twin})"
