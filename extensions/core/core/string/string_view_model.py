from blackfennec.util.observable import Observable


class StringViewModel(Observable):
    """View model for core type String."""

    def __init__(self, interpretation):
        """Create with value empty string

        Args:
            interpretation (Interpretation): The overarching
                interpretation
        """
        super().__init__()
        self._model = interpretation.structure
        self._model.structure.bind(value=self._update_value)

    @property
    def value(self):
        """Property for value"""
        return self._model.value

    @value.setter
    def value(self, value):
        self._model.value = value

    def _update_value(self, sender, new_value):
        self._notify('changed', new_value, sender)
