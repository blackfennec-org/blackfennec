from src.core.boolean import Boolean

class BooleanViewModel:
    """View model for core type Boolean."""

    def __init__(self, interpretation):
        """Create with value empty boolean
        
        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation
        """
        self._model = interpretation.info

    @property
    def value(self):
        """Property for value"""
        return self._model.value

    @value.setter
    def value(self, value):
        self._model.value = value
