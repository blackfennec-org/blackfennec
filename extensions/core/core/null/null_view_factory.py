from core.null.null_preview import NullPreview
from core.null.null_view_model import NullViewModel
from blackfennec.interpretation.interpretation import Interpretation
from blackfennec.interpretation.specification import Specification


class NullViewFactory:
    """Creator of the NullView"""

    def satisfies(self, specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            specification (Specification): the specification to be
                satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return specification.is_request_for_preview

    def create(self, interpretation: Interpretation) -> NullPreview:
        """creates a NullView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            specification (Specification): The specification which can fine
                tune the creation function.

        Returns:
            NullView
        """
        view_model = NullViewModel(interpretation)
        return NullPreview(view_model)
