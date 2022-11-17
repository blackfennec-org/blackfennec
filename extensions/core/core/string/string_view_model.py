from blackfennec.structure.string import String
from blackfennec.util.change_notification_dispatch_mixin import ChangeNotificationDispatchMixin
from blackfennec.util.observable import Observable


class StringViewModel(ChangeNotificationDispatchMixin):
    """View model for core type String."""

    def __init__(self, interpretation):
        """Create with value empty string

        Args:
            interpretation (Interpretation): The overarching
                interpretation
        """
        ChangeNotificationDispatchMixin.__init__(self)

        self._string: String = interpretation.structure
        self._string.bind(changed=self._dispatch_change_notification)

    @property
    def string(self):
        """Property for string"""
        return self._string

    @string.setter
    def string(self, string: String):
        self._string = string
