from collections import UserList

from doubles.black_fennec.structure.double_structure import StructureMock
from src.black_fennec.structure.list import List


class ListMock(UserList, StructureMock):
    def __init__(self, value=None, parent=None, root=None):
        UserList.__init__(self, value)
        StructureMock.__init__(self, value, parent, root)

    def accept(self, visitor):
        return visitor.visit_list(self)


class ListInstanceMock(List, ListMock):
    def __init__(self, value=None, parent=None, root=None):
        List.__init__(self)
        List.data = value
        ListMock.__init__(self, value, parent, root)
