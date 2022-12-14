from blackfennec.structure.null import Null
from blackfennec.util.intercepting_visitor import InterceptingVisitor

import logging

logger = logging.getLogger(__name__)


class MergedPhantom:
    """A mock object to allow navigating a phantom structure for merging"""

    def __init__(self, parent, twin):
        self._parent = parent
        self._twin = twin
        self._structure = Null()
        self._structure.parent = self._parent

    @property
    def structure(self):
        return self._structure

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

    def __eq__(self, other):
        if not isinstance(other, MergedPhantom):
            return False
        return self._twin == other._twin

    def __hash__(self):
        return hash(self._twin)

    def __repr__(self) -> str:
        return f"MergedPhantom(parent={self._parent}, twin={self._twin})"
