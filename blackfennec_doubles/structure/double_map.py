from collections import UserDict

from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec.structure.map import Map


class MapMock(StructureMock):
    def __init__(self, value: dict = None, parent=None, root=None):
        self.type_name = 'Map'
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
