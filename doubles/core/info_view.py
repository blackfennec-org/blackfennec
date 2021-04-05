# -*- coding: utf-8 -*-
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class InfoViewDummy(Gtk.Widget):
    def __init__(self):
        super().__init__()
