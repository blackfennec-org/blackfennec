# -*- coding: utf-8 -*-
import logging

from gi.repository import Gtk

from src.visualisation.base.person.person_view_model import PersonViewModel

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/visualisation/base/person/person_view.glade')
class PersonView(Gtk.Bin):
    """View for the Base type Person."""

    __gtype_name__ = 'PersonView'
    _courtesy_title_value: Gtk.Label = Gtk.Template.Child()
    _first_name_value: Gtk.Label = Gtk.Template.Child()
    _middle_name_value: Gtk.Label = Gtk.Template.Child()
    _last_name_value: Gtk.Label = Gtk.Template.Child()
    _suffix_value: Gtk.Label = Gtk.Template.Child()
    _gender_value: Gtk.Label = Gtk.Template.Child()
    _sex_value: Gtk.Label = Gtk.Template.Child()
    _marital_status_value: Gtk.Label = Gtk.Template.Child()
    _nationality_value: Gtk.Label = Gtk.Template.Child()

    def __init__(self, view_model: PersonViewModel):
        """Construct with view_model.

        Args:
            view_model (PersonViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._set_courtesy_title()
        self._set_first_name()
        self._set_middle_name()
        self._set_last_name()
        self._set_suffix()
        self._set_gender()
        self._set_sex()
        self._set_marital_status()
        self._set_nationality()
        logger.info(
            'PersonView created'
        )

    def _set_courtesy_title(self):
        courtesy_title = self._view_model.courtesy_title
        self._courtesy_title_value.set_text(str(courtesy_title))

    def _set_first_name(self):
        first_name = self._view_model.first_name
        self._first_name_value.set_text(str(first_name))

    def _set_middle_name(self):
        middle_name = self._view_model.middle_name
        self._middle_name_value.set_text(str(middle_name))

    def _set_last_name(self):
        last_name = self._view_model.last_name
        self._last_name_value.set_text(str(last_name))

    def _set_suffix(self):
        suffix = self._view_model.suffix
        self._suffix_value.set_text(str(suffix))

    def _set_gender(self):
        gender = self._view_model.gender
        self._gender_value.set_text(str(gender))

    def _set_sex(self):
        sex = self._view_model.sex
        self._sex_value.set_text(str(sex))

    def _set_marital_status(self):
        marital_status = self._view_model.marital_status
        self._marital_status_value.set_text(str(marital_status))

    def _set_nationality(self):
        nationality = self._view_model.nationality
        self._nationality_value.set_text(str(nationality))
