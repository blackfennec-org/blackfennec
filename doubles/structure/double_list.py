from collections import UserList


class ListMock(UserList):
    def __init__(self, value=None, children: list = None):
        UserList.__init__(self, children)
        self._value_property_access_count = 0
        self._value_history = [value]
        self._children_property_access_count = 0
        self._children = children

    @property
    def value(self):
        self._value_property_access_count += 1
        return self._value_history[-1]

    @value.setter
    def value(self, value):
        self._value_history.append(value)

    @property
    def children(self):
        self._children_property_access_count += 1
        return self._children
