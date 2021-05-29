class StringViewModel:
    """View model for core type String."""

    def __init__(self, interpretation):
        """Create with value empty string

        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation
        """
        self._model = interpretation.structure

    @property
    def value(self):
        """Property for value"""
        return self._model.value

    @value.setter
    def value(self, value):
        self._model.value = value
