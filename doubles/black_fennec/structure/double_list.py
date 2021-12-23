from collections import UserList

from doubles.black_fennec.structure.double_structure import StructureMock
from src.black_fennec.structure.list import List


class ListMock(StructureMock):
    def __init__(self, value=None, parent=None, root=None):
        self.type_name = 'List'
        value = value if value else list()
        StructureMock.__init__(self, value, parent, root)

    def accept(self, visitor):
        return visitor.visit_list(self)

    def add_item(self, item):
        self._value.append(item)

    def remove_item(self, item):
        self._value.remove(item)


class ListInstanceMock(List, ListMock):
    def __init__(self, value=None, parent=None, root=None):
        List.__init__(self, value)
        ListMock.__init__(self, value, parent, root)
