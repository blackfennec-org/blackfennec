import numbers

from blackfennec.util.change_notification import ChangeNotification
from blackfennec.structure.number import Number
from blackfennec.util.change_notification_dispatch_mixin import ChangeNotificationDispatchMixin
from blackfennec.util.observable import Observable


class NumberViewModel(ChangeNotificationDispatchMixin):
    """View model for core type Number."""

    def __init__(self, interpretation):
        """Create with value empty number

        Args:
            interpretation (Interpretation): The overarching
                interpretation
        """
        ChangeNotificationDispatchMixin.__init__(self)

        self._number: Number = interpretation.structure
        self._number.bind(changed=self._dispatch_change_notification)

    @property
    def number(self) -> Number:
        """Property for value of type number.Number"""
        return self._number

    @number.setter
    def number(self, number: Number):
        self._number = number
