import logging

from blackfennec.structure.boolean import Boolean
from blackfennec.util.change_notification_dispatch_mixin import ChangeNotificationDispatchMixin
from blackfennec.util.observable import Observable

logger = logging.getLogger(__name__)


class BooleanViewModel(ChangeNotificationDispatchMixin):
    """View model for core type Boolean."""

    def __init__(self, interpretation):
        """Create with value empty boolean

        Args:
            interpretation (Interpretation): The overarching
                interpretation
        """
        ChangeNotificationDispatchMixin.__init__(self)

        self._boolean = interpretation.structure
        self._boolean.bind(changed=self._dispatch_change_notification)

    @property
    def boolean(self) -> Boolean:
        """Property for value"""
        return self._boolean

    @boolean.setter
    def boolean(self, boolean):
        self._boolean = boolean
