# -*- coding: utf-8 -*-

import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class ViewFactoryMock:
    def __init__(self, view=None):
        self._view = view or Gtk.Box()
        self.create_call_count = 0

    def create(self, interpretation):
        self.create_call_count += 1
        return self._view
