from collections import UserDict

from doubles.black_fennec.structure.double_structure import StructureMock
from src.black_fennec.structure.map import Map


class MapMock(StructureMock):
    def __init__(self, value: dict = None, parent=None, root=None):
        value = value if value else dict()
        StructureMock.__init__(self, value, parent, root)

    def accept(self, visitor):
        return visitor.visit_map(self)

    def add_item(self, key, item):
        self._value[key] = item

    def remove_item(self, key):
        self._value.pop(key)


class MapInstanceMock(Map, MapMock):
    def __init__(self, value: dict = None, parent=None, root=None):
        Map.__init__(self, value)
        MapMock.__init__(self, value, parent, root)
