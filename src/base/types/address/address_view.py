# -*- coding: utf-8 -*-
import logging

from gi.repository import Gtk

from src.base.types.address.address_view_model import AddressViewModel

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/base/types/address/address_view.glade')
class AddressView(Gtk.Bin):
    """View for the core type Address."""

    __gtype_name__ = 'AddressView'
    _first_name_value: Gtk.Label = Gtk.Template.Child()
    _last_name_value: Gtk.Label = Gtk.Template.Child()
    _street_and_nr_value: Gtk.Label = Gtk.Template.Child()
    _city_value: Gtk.Label = Gtk.Template.Child()

    def __init__(self, view_model: AddressViewModel):
        """Construct with view_model.

        Args:
            view_model (AddressViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._set_first_name()
        self._set_last_name()
        self._set_street_and_nr()
        self._set_city()
        logger.info(
            'AddressView created'
        )

    def _set_first_name(self):
        first_name = self._view_model.first_name
        self._first_name_value.set_text(str(first_name))

    def _set_last_name(self):
        last_name = self._view_model.last_name
        self._last_name_value.set_text(str(last_name))

    def _set_street_and_nr(self):
        street = self._view_model.street
        street_number = self._view_model.street_number
        self._street_and_nr_value.set_text(
            str(street) + ' ' + str(street_number)
        )

    def _set_city(self):
        city = self._view_model.city
        self._city_value.set_text(str(city))

