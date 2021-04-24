from src.type_system.core.list.list_view_model import ListViewModel
from src.type_system.core.list.list_view import ListView
from src.interpretation.interpretation import Interpretation
from src.interpretation.specification import Specification

class ListViewFactory:
    """Creator of the ListView"""

    def satisfies(self, specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            specification (Specification): the specification to be satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return not specification.is_request_for_preview

    def create(self, interpretation: Interpretation,
            _: Specification) -> ListView:
        """creates a ListView

        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation.
            _ (Specification): The specification which can fine
                tune the creation function.

        Returns:
            :obj:`ListView`
        """
        view_model = ListViewModel(interpretation)
        return ListView(view_model)
