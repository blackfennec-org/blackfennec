# -*- coding: utf-8 -*-
import logging

from gi.repository import Gtk

from src.visualisation.base.person.person_view_model import PersonViewModel

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/visualisation/base/person/person_preview.glade')
class PersonPreview(Gtk.Bin):
    """View for the Base type Person."""

    __gtype_name__ = 'PersonPreview'
    _first_name_value: Gtk.Label = Gtk.Template.Child()
    _last_name_value: Gtk.Label = Gtk.Template.Child()

    def __init__(self, view_model: PersonViewModel):
        """Construct with view_model.

        Args:
            view_model (PersonViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._set_first_name()
        self._set_last_name()

        logger.info('PersonPreview created')

    def _set_first_name(self):
        first_name = self._view_model.first_name
        self._first_name_value.set_text(str(first_name))

    def _set_last_name(self):
        last_name = self._view_model.last_name
        self._last_name_value.set_text(str(last_name))

    @Gtk.Template.Callback()
    def _preview_clicked(self, unused_sender, unused_argument) -> None:
        """Handles clicks on person items, triggers navigation"""
        self._view_model.navigate()
