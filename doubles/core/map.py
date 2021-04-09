from collections import UserDict


class MapMock(UserDict):
    def __init__(self, value: dict = None):
        UserDict.__init__(self)
        self._value = {} if value is None else value
        self._value_property_access_count = 0
        self._value_history = [value]
        self._children_property_access_count = 0
        self._children = [] if value is None else value.values()

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
