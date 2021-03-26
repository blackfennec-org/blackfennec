from src.core.string import String

class StringViewModel:
    """View model for core type String."""

    def __init__(self):
        """Create with value empty string"""
        self._string = String()

    @property
    def value(self):
        """Property for value"""
        return self._string.value

    @value.setter
    def value(self, value):
        self._string.value = value
