from src.type_system.core.number.number_view_model import NumberViewModel
from src.type_system.core.number.number_view import NumberView
from src.interpretation.interpretation import Interpretation
from src.interpretation.specification import Specification


class NumberViewFactory:
    """Creator of the NumberView"""

    def satisfies(self, specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            specification (Specification): the specification to be satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return not specification.is_request_for_preview

    def create(self, interpretation: Interpretation,
            _: Specification) -> NumberView:
        """creates a NumberView

        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation.
            _ (Specification): The specification which can fine
                tune the creation function.

        Returns:
            :obj:`NumberView`
        """
        view_model = NumberViewModel(interpretation)
        return NumberView(view_model)
