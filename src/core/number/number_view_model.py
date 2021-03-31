from src.core.number import Number

class NumberViewModel:
    """View model for core type Number."""

    def __init__(self, interpretation):
        """Create with value empty number
        
        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation
        """
        self._model = Number()

    @property
    def value(self):
        """Property for value"""
        return self._model.value

    @value.setter
    def value(self, value):
        self._model.value = value
