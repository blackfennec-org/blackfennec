from src.type_system.core.reference.reference_view_model import ReferenceViewModel
from src.type_system.core.reference.reference_preview import ReferencePreview
from src.interpretation.interpretation import Interpretation
from src.interpretation.interpretation_service import InterpretationService
from src.interpretation.specification import Specification


class ReferenceViewFactory:
    """Creator of the ReferenceView"""
    def __init__(self, interpretation_service: InterpretationService):
        self._interpretation_service = interpretation_service

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
            _: Specification) -> ReferencePreview:
        """creates a ReferenceView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            _ (Specification): The specification which can fine
                tune the creation function.

        Returns:
            ReferencePreview:
        """
        view_model = ReferenceViewModel(interpretation, self._interpretation_service)
        return ReferencePreview(view_model)
