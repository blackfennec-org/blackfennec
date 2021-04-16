# -*- coding: utf-8 -*-

from src.type_system.base.address.address_view_model import AddressViewModel
from src.type_system.base.address.address_view import AddressView


class AddressViewFactory:
    """Creator of the AddressView"""

    def create(self, interpretation) -> AddressView:
        """creates a AddressView

        Args:
            interpretation (Interpretation): The overarching
                interpretation.

        Returns:
            AddressView
        """
        view_model = AddressViewModel(interpretation)
        return AddressView(view_model)
