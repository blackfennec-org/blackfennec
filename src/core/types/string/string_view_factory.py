from src.core.types.string import StringViewModel, StringView

class StringViewFactory:
    """Creator of the StringView"""

    def create(self, interpretation) -> StringView:
        """creates a StringView

        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation.

        Returns:
            :obj:`StringView`
        """
        view_model = StringViewModel(interpretation)
        return StringView(view_model)
