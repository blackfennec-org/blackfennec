# -*- coding: utf-8 -*-
import logging
from pathlib import Path
from gi.repository import Gtk, Adw

from src.visualisation.base.date_time.date_time_editor import DateTimeEditor
from src.visualisation.base.date_time.date_time_view_model import DateTimeViewModel

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('date_time_preview.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class DateTimePreview(Gtk.MenuButton):
    """View for the core type DateTime."""

    __gtype_name__ = 'DateTimePreview'
    _popover: Gtk.Popover = Gtk.Template.Child()

    def __init__(self, view_model: DateTimeViewModel):
        """Construct with view_model.

        Args:
            view_model (DateTimeViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._view_model.bind(date_time=self._set_date_time)
        self._set_date_time(self, self._view_model.date_time)
        logger.info('DateTimePreview created')

        self.set_label(str(self._view_model.date_time))
        self._date_time_editor = DateTimeEditor(self._view_model)
        self._popover.set_child(self._date_time_editor)

    def _set_date_time(self, unused_sender, date_time):
        self.set_label(str(date_time))
