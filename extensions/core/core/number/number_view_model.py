import numbers

from blackfennec.util.change_notification import ChangeNotification
from blackfennec.structure.number import Number
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

        self._number: Number = interpretation.structure
        self._number.bind(changed=self._update_value)

    @property
    def number(self) -> Number:
        """Property for value of type number.Number"""
        return self._number

    @number.setter
    def number(self, number: Number):
        self._number = number

    def _update_value(self, sender, notification: ChangeNotification):
        new_value = notification.new_value
        self._notify('changed', notification, sender)
