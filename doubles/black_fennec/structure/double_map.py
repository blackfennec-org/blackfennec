from collections import UserDict

from doubles.black_fennec.structure.double_info import InfoMock
from src.black_fennec.structure.map import Map


class MapMock(UserDict, InfoMock):
    def __init__(self, value: dict = None, parent=None, root=None):
        UserDict.__init__(self, value)
        InfoMock.__init__(self, value, parent=parent, root=root)
        self.data = {} if value is None else value
        self._children = self.data.values()

    def accept(self, visitor):
        return visitor.visit_map(self)


class MapInstanceMock(Map, MapMock):
    def __init__(self, value: dict = None, parent=None, root=None):
        Map.__init__(self)
        Map.data = value
        MapMock.__init__(self, value, parent, root)