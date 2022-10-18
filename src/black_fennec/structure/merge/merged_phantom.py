from src.black_fennec.util.intercepting_visitor import InterceptingVisitor


import logging

logger = logging.getLogger(__name__)

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
