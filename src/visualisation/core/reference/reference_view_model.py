import logging

from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.reference import Reference

logger = logging.getLogger(__name__)


class ReferenceViewModel:
    """View model for core type Reference."""

    def __init__(self, interpretation: Interpretation):
        """Create with value empty reference.

        Args:
            interpretation (Interpretation): The overarching interpretation

        Raises:
            TypeError: if passed Interpretation does not contain a Reference.
        """
        self._interpretation = interpretation
        interpretation_structure = interpretation.structure
        if isinstance(interpretation_structure, Reference):
            self._reference: Reference = interpretation_structure
        else:
            message = 'Structure contained in Interpretation has to be' \
                      ' of type Reference'
            logger.error(message)
            raise TypeError(message)

    @property
    def reference(self) -> Reference:
        """Readonly property for value."""
        return self._reference

    def navigate_to(self, route_target: Structure):
        self._interpretation.navigate(route_target)
