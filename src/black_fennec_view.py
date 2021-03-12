import logging
import gi
from gi.repository import Gtk

gi.require_version("Gtk", "3.0")

logger = logging.getLogger(__name__)


@Gtk.Template(filename="src/black_fennec.glade")
class BlackFennecView(Gtk.ApplicationWindow):
    __gtype_name__ = "BlackFennecView"

    def __init__(self, app):
        super().__init__(application=app)
        logger.info("BlackFennecView __init__")
        self._wave_button_pressed_count = 0

    @Gtk.Template.Callback()
    def on_button_clicked(self, info_presenter_view):
        logger.info("wave button has been pressed")
        self._wave_button_pressed_count += 1
        logger.debug("wave button click count: %i",
                     self._wave_button_pressed_count)
