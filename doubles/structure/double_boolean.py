class BooleanMock:
    def __init__(self, value = False):
        self._value = value
        self._value_property_access_count = 0

    @property
    def value(self):
        self._value_property_access_count += 1
        return self._value
