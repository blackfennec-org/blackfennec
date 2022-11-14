from blackfennec.structure.string import String
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
        self._string: String = interpretation.structure
        self._string.bind(changed=self._update_value)

    @property
    def string(self):
        """Property for string"""
        return self._string

    @string.setter
    def string(self, string: String):
        self._string = string

    def _update_value(self, sender, notification):
        new_value = notification.new_value
        assert self.string.structure.value == new_value
        self._notify('changed', notification, sender)
