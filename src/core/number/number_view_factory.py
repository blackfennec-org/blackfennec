from src.core.number import NumberViewModel, NumberView

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
