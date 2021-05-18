from src.visualisation.core.list.list_view_model import ListViewModel
from src.visualisation.core.list.list_view import ListView
from src.visualisation.core.list.list_preview import ListPreview
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.interpretation_service import InterpretationService
from src.black_fennec.interpretation.specification import Specification


class ListViewFactory:
    """Creator of the ListView"""
    def __init__(self, interpretation_service: InterpretationService):
        self._interpretation_service = interpretation_service

    def satisfies(self, unused_specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            unused_specification (Specification): the specification to be
                satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return True

    def create(self, interpretation: Interpretation,
               specification: Specification) -> ListView:
        """creates a ListView

        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation.
            specification (Specification): The specification which can fine
                tune the creation function.

        Returns:
            :obj:`ListView`
        """
        view_model = ListViewModel(interpretation, self._interpretation_service)
        if specification.is_request_for_preview:
            return ListPreview(view_model)
        return ListView(view_model)
