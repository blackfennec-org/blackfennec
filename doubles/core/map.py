from collections import UserDict

class MapMock(UserDict):
    def __init__(self, value = None):
        UserDict.__init__(self)
        self._value = {} if value is None else value
        self._value_property_access_count = 0

    @property
    def value(self):
        self._value_property_access_count += 1
        return self._value
