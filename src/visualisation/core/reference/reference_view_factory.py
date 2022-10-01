import logging

from src.visualisation.core.reference.reference_view_model import ReferenceViewModel
from src.visualisation.core.reference.reference_preview import ReferencePreview
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.specification import Specification

logger = logging.getLogger(__name__)


class ReferenceViewFactory:
    """View Factory of Reference CoreType"""

    def satisfies(self, specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            specification (Specification): the specification to be
                satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return specification.is_request_for_preview

    def create(self, interpretation: Interpretation) -> ReferencePreview:
        """creates a ReferenceView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            specification (Specification): The specification which can fine
                tune the creation function.

        Returns:
            ReferencePreview: View that is used as the Preview
                of a Reference

        Raises:
            NotImplementedError: if the specification requires
                a View instead of the Preview.
        """
        if not interpretation.specification.is_request_for_preview:
            message = 'View for References not implemented'
            logger.error(message)
            raise NotImplementedError(message)
        view_model = ReferenceViewModel(
            interpretation
        )
        return ReferencePreview(view_model)
