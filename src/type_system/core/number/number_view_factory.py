from src.type_system.core.number.number_view_model import NumberViewModel
from src.type_system.core.number.number_view import NumberView


class NumberViewFactory:
    """Creator of the NumberView"""

    def create(self, interpretation) -> NumberView:
        """creates a NumberView

        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation.

        Returns:
            :obj:`NumberView`
        """
        view_model = NumberViewModel(interpretation)
        return NumberView(view_model)
