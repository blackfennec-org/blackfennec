from src.black_fennec.structure.visitor import Visitor
from src.black_fennec.structure.structure import Structure
from src.black_fennec.util.intercepting_visitor import InterceptingVisitor
import src.black_fennec.structure.merge.deep_merge as deep_merge

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

class MergedList(MergedStructure):
    def __init__(self, underlay: Structure, overlay: Structure):
        super().__init__(underlay, overlay)
        logger.warning("MergedList is not implemented")

    @property
    def value(self):
        raise NotImplementedError("MergedList does not support value")

    @value.setter
    def value(self, value):
        raise AssertionError("Cannot set value on merged layer")


class MergedMap(MergedStructure):
    def __init__(self, underlay: Structure, overlay: Structure):
        super().__init__(underlay, overlay)

    @property
    def value(self):
        result = {}
        for key, value in self._underlay.value.items():
            if key in self._overlay.value:
                result[key] = deep_merge.DeepMerge.merge(value, self._overlay.value[key])
            else:
                result[key] = deep_merge.DeepMerge.merge(value, MergedPhantom(self._overlay, value))

        for key, value in self._overlay.value.items():
            if key not in self._underlay.value:
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
        if self._overlay.value is not None:
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

    def parent(self):
        return self._parent

    def accept(self, visitor):
        return self._twin.accept(visitor)

    def __bool__(self):
        return False
