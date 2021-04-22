from src.type_system.core.boolean.boolean_view_model import BooleanViewModel
from src.type_system.core.boolean.boolean_view import BooleanView
from src.interpretation.interpretation import Interpretation
from src.interpretation.specification import Specification

class BooleanViewFactory:
    """Creator of the BooleanView"""

    def satisfies(self, specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            specification (Specification): the specification to be satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return not specification.is_request_for_preview

    def create(self, interpretation: Interpretation,
            _: Specification) -> BooleanView:
        """creates a BooleanView

        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation.
            specification (Specification): The specification which can fine
                tune the creation function.

        Returns:
            :obj:`BooleanView`
        """
        view_model = BooleanViewModel(interpretation)
        return BooleanView(view_model)
