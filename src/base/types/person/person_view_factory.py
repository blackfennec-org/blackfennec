# -*- coding: utf-8 -*-

from src.base.types.person.person_view_model import PersonViewModel
from src.base.types.person.person_view import PersonView


class PersonViewFactory:
    """Creator of the PersonView"""

    def create(self, interpretation) -> PersonView:
        """creates a PersonView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.

        Returns:
            PersonView
        """
        view_model = PersonViewModel(interpretation)
        return PersonView(view_model)
