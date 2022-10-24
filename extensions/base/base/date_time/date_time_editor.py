# -*- coding: utf-8 -*-
import logging
from datetime import datetime
from pathlib import Path

import gi

from base.date_time.date_time_view_model import DateTimeViewModel

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Adw, Gio, GLib

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('date_time_editor.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class DateTimeEditor(Gtk.Box):
    __gtype_name__ = 'DateTimeEditor'

    _date_chooser: Gtk.Calendar = Gtk.Template.Child()
    _hour: Gtk.Text = Gtk.Template.Child()
    _minute: Gtk.Text = Gtk.Template.Child()
    _second: Gtk.Text = Gtk.Template.Child()

    def __init__(self, view_model: DateTimeViewModel):
        super().__init__()
        self._view_model = view_model
        self._view_model.bind(date_time=self.update_date_time)

        self._date_chooser.connect('day-selected', self._on_day_selected)
        self.update_date_time(self, self._view_model.date_time)

        self.hour = self._view_model.date_time.hour
        self.minute = self._view_model.date_time.minute
        self.second = self._view_model.date_time.second

    def update_date_time(self, unused_sender, date_time: datetime):
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
        self._date_chooser.select_day(g_date_time)

    @property
    def hour(self) -> int:
        return self._hour.get_text()

    @hour.setter
    def hour(self, value):
        if value > 23:
            value = 23
            self._hour.set_text(str(value))
        self._view_model.date_time = self._view_model.date_time.replace(hour=value)

    @property
    def minute(self) -> int:
        return self._minute.get_text()

    @minute.setter
    def minute(self, value):
        if value > 59:
            value = 59
            self._minute.set_text(str(value))
        self._view_model.date_time = self._view_model.date_time.replace(minute=value)

    @property
    def second(self) -> int:
        return self._second.get_text()

    @second.setter
    def second(self, value):
        if value > 59:
            value = 59
            self._second.set_text(str(value))
        self._view_model.date_time = self._view_model.date_time.replace(second=value)

    def _on_day_selected(self, unused_widget):
        date_time: GLib.DateTime = self._date_chooser.get_date()
        picked_date = self._view_model.date_time.replace(
            date_time.get_year(),
            date_time.get_month(),
            date_time.get_day_of_month()
        )
        if not self._view_model.date_time == picked_date:
            self._view_model.date_time = picked_date

    @Gtk.Template.Callback()
    def _on_set_to_now(self, unused_widget):
        now = datetime.now()
        if now.microsecond >= 500_000:
            now = now.replace(second=now.second + 1)
        self._view_model.date_time = now.replace(microsecond=0)
        self._hour.set_text(str(now.hour).zfill(2))
        self._minute.set_text(str(now.minute).zfill(2))
        self._second.set_text(str(now.second).zfill(2))

    @Gtk.Template.Callback()
    def _on_hour_changed(self, unused_widget):
        if not self._view_model.date_time.minute == self.hour and len(self._hour.get_text()) == 2:
            self.hour = int(self.hour)

    @Gtk.Template.Callback()
    def _on_minute_changed(self, unused_widget):
        if not self._view_model.date_time.minute == self.minute and len(self._minute.get_text()) == 2:
            self.minute = int(self.minute)

    @Gtk.Template.Callback()
    def _on_second_changed(self, unused_widget):
        if not self._view_model.date_time.second == self.second and len(self._second.get_text()) == 2:
            self.second = int(self.second)
