from src.black_fennec.structure.visitor import Visitor
from src.black_fennec.structure.structure import Structure
import src.black_fennec.structure.merge.deep_merge as deep_merge
from src.black_fennec.util.intercepting_visitor import InterceptingVisitor


import logging
logger = logging.getLogger(__name__)


class MergedStructure:
    def __init__(self, underlay: Structure, overlay: Structure):
        self._underlay = underlay
        self._overlay = overlay

    @property
    def subject(self):
        raise AssertionError("Subject of a merged structure is not defined.")

    @subject.setter
    def subject(self, value: Structure):
        raise AssertionError("Subject of MergedStructure cannot be set")

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
            assert self._underlay.parent
            return deep_merge.DeepMerge.merge(self._underlay.parent, self._overlay.parent)

    @parent.setter
    def parent(self, parent: Structure):
        raise AssertionError("Cannot set parent on MergedStructure")

    @property
    def root(self):
        return deep_merge.DeepMerge.merge(self._underlay.root, self._overlay.root)

    def __repr__(self) -> str:
        return f"MergedStructure(underlay={self._underlay}, overlay={self._overlay})"

    def __eq__(self, o):
        if not isinstance(o, MergedStructure):
            return False
        return self._underlay == o._underlay and self._overlay == o._overlay

    def __ne__(self, other) -> bool:
        return not self == other


class MergedList(MergedStructure):
    def __init__(self, underlay: Structure, overlay: Structure):
        super().__init__(underlay, overlay)
        logger.warning("MergedList is not implemented")

    @property
    def value(self):
        logger.warning("Accessed value of merged list: implementation is disputed")
        return [ deep_merge.DeepMerge.merge(MergedPhantom(self, child), child) 
            for child in self._underlay.value + self._overlay.value ]

    @value.setter
    def value(self, value):
        raise AssertionError("Cannot set value on merged layer")


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
    def value(self):
        if self._overlay and self._overlay.value is not None:
            return self._overlay.value
        return self._underlay.value

    @value.setter
    def value(self, value):
        raise AssertionError("Value cannot be set on MergedStructure")


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
