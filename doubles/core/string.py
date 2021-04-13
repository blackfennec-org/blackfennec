class StringMock:
    def __init__(self, value = None):
        self._value = '' if value is None else value
        self._value_property_access_count = 0
        self._parent_property_getter_count = 0
        self._parent_property_setter_count = 0
        self._parent = None

    @property
    def parent(self):
        self._parent_property_getter_count += 1
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value
        self._parent_property_setter_count += 1

    @property
    def value(self):
        self._value_property_access_count += 1
        return self._value

    def __eq__(self, other):
        return (self.value, self.parent) == (other.value, other.parent)

    def __str__(self):
        return self._value
