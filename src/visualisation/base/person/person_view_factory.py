# -*- coding: utf-8 -*-
from src.visualisation.base.person.person_preview import PersonPreview
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
        return True

    def create(self, interpretation: Interpretation,
               specification: Specification) -> PersonView:
        """creates a PersonView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            specification (Specification): The specification which can fine
                tune the creation function.

        Returns:
            PersonView
        """
        view_model = PersonViewModel(interpretation)

        if specification.is_request_for_preview:
            return PersonPreview(view_model)

        return PersonView(view_model)
