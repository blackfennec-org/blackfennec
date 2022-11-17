import logging

from blackfennec.interpretation.interpretation import Interpretation
from blackfennec.structure.reference import Reference
from blackfennec.util.change_notification_dispatch_mixin import ChangeNotificationDispatchMixin
from blackfennec.util.observable import Observable

logger = logging.getLogger(__name__)


class ReferenceViewModel(ChangeNotificationDispatchMixin):
    """View model for core type Reference."""

    def __init__(self, interpretation: Interpretation):
        """Create with value empty reference.

        Args:
            interpretation (Interpretation): The overarching interpretation

        Raises:
            TypeError: if passed Interpretation does not contain a Reference.
        """
        ChangeNotificationDispatchMixin.__init__(self)

        self._interpretation = interpretation

        self._reference: Reference = interpretation.structure
        self._reference.bind(changed=self._dispatch_change_notification)

    @property
    def reference(self) -> Reference:
        """Readonly property for value."""
        return self._reference

    def navigate_to_reference(self):
        self._interpretation.navigate(self._reference.resolve())
