from src.type_system.core.string.string_view_model import StringViewModel
from src.type_system.core.string.string_view import StringView

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
