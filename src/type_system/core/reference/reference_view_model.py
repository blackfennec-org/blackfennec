import logging

from src.structure.info import Info
from src.navigation.navigation_proxy import NavigationProxy
from src.interpretation.specification import Specification
from src.interpretation.interpretation import Interpretation
from src.structure.reference import Reference

logger = logging.getLogger(__name__)


class ReferenceViewModel:
    """View model for core type Reference."""

    def __init__(self, interpretation, interpretation_service):
        """Create with value empty reference.

        Args:
            interpretation (Interpretation): The overarching interpretation
            interpretation_service (InterpretationService): service to
                interpret substructures and create previews
        """
        self._interpretation = interpretation
        self._interpretation_service = interpretation_service
        interpretation_info = interpretation.info
        if isinstance(interpretation_info, Reference):
            self._reference: Reference = interpretation_info
        else:
            message = 'Info contained in Interpretation has to be of type Reference'
            logger.error(message)
            raise TypeError(message)

    @property
    def reference(self) -> Reference:
        """Readonly property for value."""
        return self._reference

    def navigate_to(self, route_target: Info):
        self._interpretation.navigate(route_target)
