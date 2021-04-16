# -*- coding: utf-8 -*-
import logging

from gi.repository import Gtk

from src.type_system.base.date_time.date_time_view_model import DateTimeViewModel

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/type_system/base/date_time/date_time_view.glade')
class DateTimeView(Gtk.Bin):
    """View for the core type DateTime."""

    __gtype_name__ = 'DateTimeView'
    _date_time_value: Gtk.Label = Gtk.Template.Child()

    def __init__(self, view_model: DateTimeViewModel):
        """Construct with view_model.

        Args:
            view_model (DateTimeViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._set_date_time()
        logger.info(
            'DateTimeView created'
        )

    def _set_date_time(self):
        date_time = self._view_model.date_time
        self._date_time_value.set_text(str(date_time))
