from collections import UserList

class ListMock(UserList):
    def __init__(self, value = None):
        UserList.__init__(self)
        self._value = [] if value is None else value
        self._value_property_access_count = 0

    @property
    def value(self):
        self._value_property_access_count += 1
        return self._value
