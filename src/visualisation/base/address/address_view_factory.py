# -*- coding: utf-8 -*-

from src.visualisation.base.address.address_view_model import AddressViewModel
from src.visualisation.base.address.address_view import AddressView
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.specification import Specification


class AddressViewFactory:
    """Creator of the AddressView"""

    def satisfies(self, specification: Specification) -> bool:
        """Test if this view factory can satisfy the specification

        Args:
            specification (Specification): the specification to be satisfied

        Returns:
            bool: True if the specification can be satisfied. Otherwise False.
        """
        return not specification.is_request_for_preview

    def create(self, interpretation: Interpretation) -> AddressView:
        """creates an AddressView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.
            _ (Specification): The specification which can fine
                tune the creation function.

        Returns:
            AddressView
        """
        view_model = AddressViewModel(interpretation)
        return AddressView(view_model)
