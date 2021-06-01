# -*- coding: utf-8 -*-
import logging

from gi.repository import Gtk

from src.visualisation.base.date_time_range.date_time_range_view_model import DateTimeRangeViewModel

logger = logging.getLogger(__name__)


@Gtk.Template(filename=
              'src/visualisation/base/date_time_range/date_time_range_preview.glade')
class DateTimeRangePreview(Gtk.Bin):
    """Preview for the core type DateTimeRange."""

    __gtype_name__ = 'DateTimeRangePreview'
    _date_time_range_value: Gtk.Label = Gtk.Template.Child()

    def __init__(self, view_model: DateTimeRangeViewModel):
        """Construct with view_model.

        Args:
            view_model (DateTimeRangeViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._set_date_time()
        logger.info('DateTimeRangeView created')

    def _set_date_time(self):
        start = self._view_model.date_time_start
        end = self._view_model.date_time_end
        text = f'{start} - {end}'
        self._date_time_range_value.set_text(text)

    @Gtk.Template.Callback()
    def _preview_clicked(self, unused_sender, unused_argument) -> None:
        """Handles clicks on date_time_range items, triggers navigation"""
        self._view_model.navigate()
