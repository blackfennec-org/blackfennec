from collections import UserList

from doubles.black_fennec.structure.double_info import InfoMock
from src.black_fennec.structure.list import List


class ListMock(UserList, InfoMock):
    def __init__(self, value=None, children: list = None, parent=None, root=None):
        UserList.__init__(self, children)
        InfoMock.__init__(self, value, children, parent, root)

    def accept(self, visitor):
        return visitor.visit_list(self)


class ListInstanceMock(List, ListMock):
    def __init__(self, value=None, children: list = None, parent=None, root=None):
        List.__init__(self)
        List.data = children
        ListMock.__init__(self, value, children, parent, root)
