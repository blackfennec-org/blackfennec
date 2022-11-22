from blackfennec.structure.string import String
from blackfennec.util.change_notification_dispatch_mixin import ChangeNotificationDispatchMixin


class StringViewModel(ChangeNotificationDispatchMixin):
    """View model for core type String."""

    def __init__(self, interpretation):
        """Create with value empty string

        Args:
            interpretation (Interpretation): The overarching
                interpretation
        """
        super().__init__()

        self._string: String = interpretation.structure
        self._string.bind(changed=self._dispatch_change_notification)

    @property
    def string(self):
        """Property for string"""
        return self._string

    @string.setter
    def string(self, string: String):
        self._string = string

    @property
    def value(self):
        return self.string.value

    @value.setter
    def value(self, value):
        if self.value == value:
            return

        self.string.value = value
