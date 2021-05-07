import logging

from src.type_system.core.reference.reference_view_model import ReferenceViewModel
from src.type_system.core.reference.reference_preview import ReferencePreview
from src.interpretation.interpretation import Interpretation
from src.interpretation.specification import Specification

logger = logging.getLogger(__name__)


class ReferenceViewFactory:
    def satisfies(self, specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            specification (Specification): the specification to be
                satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return specification.is_request_for_preview

    def create(self, interpretation: Interpretation,
            specification: Specification) -> ReferencePreview:
        """creates a ReferenceView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            _ (Specification): The specification which can fine
                tune the creation function.

        Returns:
            ReferencePreview:
        """
        if not specification.is_request_for_preview:
            message = 'View for References not implemented'
            logger.error(message)
            raise NotImplementedError(message)
        view_model = ReferenceViewModel(
            interpretation
        )
        return ReferencePreview(view_model)
