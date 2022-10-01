from src.visualisation.core.map.map_view_model import MapViewModel
from src.visualisation.core.map.map_view import MapView
from src.visualisation.core.map.map_preview import MapPreview
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.interpretation_service import InterpretationService
from src.black_fennec.interpretation.specification import Specification
from src.black_fennec.type_system.template_registry import TemplateRegistry


class MapViewFactory:
    """Creator of the MapView"""

    def __init__(self,
                 interpretation_service: InterpretationService,
                 template_registry: TemplateRegistry,
                 view_factory):
        self._interpretation_service = interpretation_service
        self._template_registry = template_registry
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
            self._template_registry)
        if interpretation.specification.is_request_for_preview:
            return MapPreview(view_model)
        return MapView(self._view_factory, view_model)
