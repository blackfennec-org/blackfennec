import numbers

from blackfennec.util.change_notification import ChangeNotification
from blackfennec.util.observable import Observable


class NumberViewModel(Observable):
    """View model for core type Number."""

    def __init__(self, interpretation):
        """Create with value empty number

        Args:
            interpretation (Interpretation): The overarching
                interpretation
        """
        super().__init__()

        self._model = interpretation.structure
        self._model.structure.bind(changed=self._update_value)

    @property
    def value(self) -> numbers.Number:
        """Property for value of type number.Number"""
        return self._model.value

    @value.setter
    def value(self, value: numbers.Number):
        self._model.value = value

    def _update_value(self, sender, notification: ChangeNotification):
        self._notify('changed', notification, sender)
