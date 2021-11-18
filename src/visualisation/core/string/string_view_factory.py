from src.visualisation.core.string.string_view_model import StringViewModel
from src.visualisation.core.string.string_view import StringView
from src.visualisation.core.string.string_preview import StringPreview
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.specification import Specification


class StringViewFactory:
    """Creator of the StringView"""

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
               specification: Specification) -> StringView:
        """creates a StringView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            specification (Specification): The specification which can fine
                tune the creation function.

        Returns:
            StringView
        """
        view_model = StringViewModel(interpretation)
        if specification.is_request_for_preview:
            return StringPreview(view_model)
        return StringView(view_model)
