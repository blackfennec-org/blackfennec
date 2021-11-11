from src.visualisation.core.boolean.boolean_preview import BooleanPreview
from src.visualisation.core.boolean.boolean_view_model import BooleanViewModel
from src.visualisation.core.boolean.boolean_view import BooleanView
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.specification import Specification


class BooleanViewFactory:
    """Creator of the BooleanView"""

    def satisfies(self, unused_specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            unused_specification (Specification): the specification
            to be satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return True

    def create(self, interpretation: Interpretation,
               specification: Specification) -> BooleanView:
        """creates a BooleanView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            specification (Specification): The specification which can fine
                tune the creation function.

        Returns:
            BooleanView
        """
        view_model = BooleanViewModel(interpretation)
        if specification.is_request_for_preview:
            return BooleanPreview(view_model)
        return BooleanView(view_model)
