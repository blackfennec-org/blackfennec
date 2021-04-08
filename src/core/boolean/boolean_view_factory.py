from src.core.boolean import BooleanViewModel, BooleanView


class BooleanViewFactory:
    """Creator of the BooleanView"""

    def create(self, interpretation) -> BooleanView:
        """creates a BooleanView

        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation.

        Returns:
            :obj:`BooleanView`
        """
        view_model = BooleanViewModel(interpretation)
        return BooleanView(view_model)
