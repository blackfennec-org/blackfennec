# -*- coding: utf-8 -*-

from src.visualisation.base.person.person_view_model import PersonViewModel
from src.visualisation.base.person.person_view import PersonView
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.specification import Specification


class PersonViewFactory:
    """Creator of the PersonView"""

    def satisfies(self, specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            specification (Specification): the specification to be satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return not specification.is_request_for_preview

    def create(self, interpretation: Interpretation,
            _: Specification) -> PersonView:
        """creates a PersonView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            _ (Specification): The specification which can fine
                tune the creation function.

        Returns:
            PersonView
        """
        view_model = PersonViewModel(interpretation)
        return PersonView(view_model)
