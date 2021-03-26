from src.core.string import String

class StringViewModel:
    """View model for core type String."""

    def __init__(self, interpretation):
        """Create with value empty string
        
        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation
        """
        self._string = String()

    @property
    def value(self):
        """Property for value"""
        return self._string.value

    @value.setter
    def value(self, value):
        self._string.value = value
