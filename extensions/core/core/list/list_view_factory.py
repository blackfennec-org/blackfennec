from blackfennec.actions import ActionRegistry
from blackfennec.type_system.type_registry import TypeRegistry
from core.list.list_view_model import ListViewModel
from core.list.list_view import ListView
from core.list.list_preview import ListPreview
from blackfennec.interpretation.interpretation import Interpretation
from blackfennec.interpretation.interpretation_service import InterpretationService
from blackfennec.interpretation.specification import Specification


class ListViewFactory:
    """Creator of the ListView"""

    def __init__(
            self,
            interpretation_service: InterpretationService,
            type_registry: TypeRegistry,
            action_registry: ActionRegistry,
            view_factory
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

    def create(self, interpretation: Interpretation) -> ListView:
        """creates a ListView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            specification (Specification): The specification which can fine
                tune the creation function.

        Returns:
            ListView: with created view model contained.
        """
        view_model = ListViewModel(
            interpretation,
            self._interpretation_service,
            self._type_registry,
            self._action_registry,
        )
        if interpretation.specification.is_request_for_preview:
            return ListPreview(view_model)
        return ListView(self._view_factory, view_model)
