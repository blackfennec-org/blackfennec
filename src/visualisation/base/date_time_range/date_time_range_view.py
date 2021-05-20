# -*- coding: utf-8 -*-
import logging

from gi.repository import Gtk

from src.visualisation.base.date_time_range.date_time_range_view_model import DateTimeRangeViewModel

logger = logging.getLogger(__name__)


@Gtk.Template(filename=
              'src/visualisation/base/date_time_range/date_time_range_view.glade')
class DateTimeRangeView(Gtk.Bin):
    """View for the core type DateTimeRange."""

    __gtype_name__ = 'DateTimeRangeView'
    _date_time_range_start_value: Gtk.Label = Gtk.Template.Child()
    _date_time_range_end_value: Gtk.Label = Gtk.Template.Child()

    def __init__(self, view_model: DateTimeRangeViewModel):
        """Construct with view_model.

        Args:
            view_model (DateTimeRangeViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._set_date_time_start()
        self._set_date_time_end()
        logger.info(
            'DateTimeRangeView created'
        )

    def _set_date_time_start(self):
        date_time = self._view_model.date_time_start
        self._date_time_range_start_value.set_text(str(date_time))

    def _set_date_time_end(self):
        date_time = self._view_model.date_time_end
        self._date_time_range_end_value.set_text(str(date_time))
