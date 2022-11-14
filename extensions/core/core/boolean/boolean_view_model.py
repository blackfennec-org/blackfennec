import logging

from blackfennec.structure.boolean import Boolean
from blackfennec.util.observable import Observable

logger = logging.getLogger(__name__)


class BooleanViewModel(Observable):
    """View model for core type Boolean."""

    def __init__(self, interpretation):
        """Create with value empty boolean

        Args:
            interpretation (Interpretation): The overarching
                interpretation
        """
        super().__init__()

        self._boolean = interpretation.structure
        self._boolean.bind(changed=self._update_value)

    @property
    def boolean(self) -> Boolean:
        """Property for value"""
        return self._boolean

    @boolean.setter
    def boolean(self, boolean):
        self._boolean = boolean

    def _update_value(self, sender, notification):
        new_value = notification.new_value
        assert self.boolean.structure.value == new_value
        self._notify('changed', new_value, sender)
