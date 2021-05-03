from src.type_system.core.number.number_preview import NumberPreview
from src.type_system.core.number.number_view_model import NumberViewModel
from src.type_system.core.number.number_view import NumberView
from src.interpretation.interpretation import Interpretation
from src.interpretation.specification import Specification


class NumberViewFactory:
    """Creator of the NumberView"""

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
               specification: Specification) -> NumberView:
        """creates a NumberView

        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation.
            specification (Specification): The specification which can fine
                tune the creation function.

        Returns:
            :obj:`NumberView`
        """
        view_model = NumberViewModel(interpretation)
        if specification.is_request_for_preview:
            return NumberPreview(view_model)
        return NumberView(view_model)
