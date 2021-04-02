class InfoMock:
    def __init__(self, value = None):
        self.root = None
        self.parent = None
        self._value_property_access_count = 0
        self._value_history = [value]

    @property
    def value(self):
        self._value_property_access_count += 1
        return self._value_history[-1]

    @value.setter
    def value(self, value):
        self._value_history.append(value)
