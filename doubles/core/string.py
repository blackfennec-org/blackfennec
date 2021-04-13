class StringMock:
    def __init__(self, value = None):
        self._value = '' if value is None else value
        self._value_property_access_count = 0

    @property
    def value(self):
        self._value_property_access_count += 1
        return self._value
