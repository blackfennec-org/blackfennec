from blackfennec.actions import ActionRegistry
from core.map.map_view_model import MapViewModel
from core.map.map_view import MapView
from core.map.map_preview import MapPreview
from blackfennec.interpretation.interpretation import Interpretation
from blackfennec.interpretation.interpretation_service import InterpretationService
from blackfennec.interpretation.specification import Specification
from blackfennec.type_system.type_registry import TypeRegistry


class MapViewFactory:
    """Creator of the MapView"""

    def __init__(
            self,
            interpretation_service: InterpretationService,
            type_registry: TypeRegistry,
            action_registry: ActionRegistry,
            view_factory,
    ):
        self._interpretation_service = interpretation_service
        self._type_registry = type_registry
        self._action_registry = action_registry
        self._view_factory = view_factory

    def satisfies(self, unused_specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            unused_specification (Specification): the specification to be
                satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return True

    def create(self, interpretation: Interpretation) -> MapView:
        """creates a MapView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            specification (Specification): The specification which can fine
                tune the creation function.

        Returns:
            MapView: with created view model contained.
        """
        view_model = MapViewModel(
            interpretation,
            self._interpretation_service,
            self._type_registry,
            self._action_registry,
        )
        if interpretation.specification.is_request_for_preview:
            return MapPreview(view_model)
        return MapView(self._view_factory, view_model)
