# -*- coding: utf-8 -*-
import logging

from gi.repository import Gtk

from src.visualisation.base.date_time.date_time_view_model import DateTimeViewModel

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/visualisation/base/date_time/date_time_preview.glade')  # pylint:disable=line-too-long
class DateTimePreview(Gtk.Bin):
    """View for the core type DateTime."""

    __gtype_name__ = 'DateTimePreview'
    _date_time_value: Gtk.Label = Gtk.Template.Child()

    def __init__(self, view_model: DateTimeViewModel):
        """Construct with view_model.

        Args:
            view_model (DateTimeViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._set_date_time()
        logger.info('DateTimePreview created')

    def _set_date_time(self):
        date_time = self._view_model.date_time
        self._date_time_value.set_text(str(date_time))

    @Gtk.Template.Callback()
    def _preview_clicked(self, unused_sender, unused_argument) -> None:
        """Handles clicks on date_time items, triggers navigation"""
        self._view_model.navigate()
