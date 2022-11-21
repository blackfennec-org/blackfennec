# -*- coding: utf-8 -*-
import logging
from datetime import datetime
from pathlib import Path

import gi

from base.date_time.date_time_view_model import DateTimeViewModel

from blackfennec.util.change_notification import ChangeNotification

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Adw, Gio, GLib

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('date_time_editor.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class DateTimeEditor(Gtk.Box):
    __gtype_name__ = 'DateTimeEditor'

    _date_chooser: Gtk.Calendar = Gtk.Template.Child()
    _hour_entry: Gtk.Entry = Gtk.Template.Child()
    _minute_entry: Gtk.Entry = Gtk.Template.Child()
    _second_entry: Gtk.Entry = Gtk.Template.Child()

    def __init__(self, view_model: DateTimeViewModel):
        super().__init__()
        self._view_model = view_model
        self._view_model.bind(changed=self.update_date_time)

        self._date_chooser.connect('day-selected', self._on_day_selected)
        self._enable_time_change_listener = True

        self.update_date_time()

    def update_date_time(
            self,
            unused_sender=None,
            unused_notification: ChangeNotification = None,
    ):
        date_time = self._view_model.date_time
        time_zone = GLib.TimeZone.new(date_time.tzname())
        g_date_time = GLib.DateTime.new(
            time_zone,
            date_time.year,
            date_time.month,
            date_time.day,
            date_time.hour,
            date_time.minute,
            date_time.second
        )
        self._enable_time_change_listener = False

        self._date_chooser.select_day(g_date_time)
        self.hour = date_time.hour
        self.minute = date_time.minute
        self.second = date_time.second

        self._enable_time_change_listener = True

    @property
    def hour(self) -> int:
        text = self._hour_entry.get_text()
        digits_string = ''.join([i for i in text if i in '0123456789'])
        value = int(digits_string or 0)
        if value > 23:
            value = 23
        if value < 0:
            value = 0
        return value

    @hour.setter
    def hour(self, value: int):
        self._hour_entry.set_text(str(value).zfill(2))

    @property
    def minute(self) -> int:
        text = self._minute_entry.get_text()
        digits_string = ''.join([i for i in text if i in '0123456789'])
        value = int(digits_string or 0)
        if value > 59:
            value = 59
        if value < 0:
            value = 0
        return value

    @minute.setter
    def minute(self, value: int):
        self._minute_entry.set_text(str(value).zfill(2))

    @property
    def second(self) -> int:
        text = self._second_entry.get_text()
        digits_string = ''.join([i for i in text if i in '0123456789'])
        value = int(digits_string or 0)
        if value > 59:
            value = 59
        if value < 0:
            value = 0
        return value

    @second.setter
    def second(self, value: int):
        self._second_entry.set_text(str(value).zfill(2))

    def _on_day_selected(self, unused_widget):
        if self._enable_time_change_listener:
            date_time: GLib.DateTime = self._date_chooser.get_date()
            picked_date = self._view_model.date_time.replace(
                date_time.get_year(),
                date_time.get_month(),
                date_time.get_day_of_month()
            )
            self._view_model.date_time = picked_date

    @Gtk.Template.Callback()
    def _on_set_to_now(self, unused_widget):
        now = datetime.now()
        if now.microsecond >= 500_000:
            now = now.replace(second=now.second + 1)
        self._view_model.date_time = now.replace(microsecond=0)

    @Gtk.Template.Callback()
    def _on_time_changed(self, unused_widget):
        if self._enable_time_change_listener and \
                len(self._second_entry.get_text()) == \
                len(self._minute_entry.get_text()) == \
                len(self._hour_entry.get_text()) == 2:
            new = self._view_model.date_time.replace(
                second=self.second,
                minute=self.minute,
                hour=self.hour)
            self._view_model.date_time = new
