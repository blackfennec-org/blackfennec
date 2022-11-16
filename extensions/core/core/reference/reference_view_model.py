import logging

from blackfennec.interpretation.interpretation import Interpretation
from blackfennec.structure.reference import Reference
from blackfennec.util.observable import Observable

logger = logging.getLogger(__name__)


class ReferenceViewModel(Observable):
    """View model for core type Reference."""

    def __init__(self, interpretation: Interpretation):
        """Create with value empty reference.

        Args:
            interpretation (Interpretation): The overarching interpretation

        Raises:
            TypeError: if passed Interpretation does not contain a Reference.
        """
        super().__init__()
        self._interpretation = interpretation

        self._reference: Reference = interpretation.structure
        self._reference.bind(changed=self._update_value)

    @property
    def reference(self) -> Reference:
        """Readonly property for value."""
        return self._reference

    def navigate_to_reference(self):
        self._interpretation.navigate(self._reference.resolve())

    def _update_value(self, sender, notification):
        new_value = notification.new_value
        self._notify('changed', notification, sender)
