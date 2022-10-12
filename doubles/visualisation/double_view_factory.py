# -*- coding: utf-8 -*-
from gi.repository import Gtk


class ViewFactoryMock:
    def __init__(self, view=None):
        self._view = view or Gtk.Box()
        self.create_call_count = 0

    def create(self, interpretation):
        self.create_call_count += 1
        return self._view
