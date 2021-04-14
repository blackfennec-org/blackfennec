import numbers


class NumberViewModel:
    """View model for core type Number."""

    def __init__(self, interpretation):
        """Create with value empty number

        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation
        """
        self._model = interpretation.info

    @property
    def value(self) -> numbers.Number:
        """Property for value of type number.Number"""
        return self._model.value

    @value.setter
    def value(self, value: numbers.Number):
        self._model.value = value
