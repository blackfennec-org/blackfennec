import logging
from gi.repository import Gtk
from src.core.string import StringViewFactory
from src.core.map import MapViewFactory

logger = logging.getLogger(__name__)

@Gtk.Template(filename="src/black_fennec.glade")
class BlackFennecView(Gtk.ApplicationWindow):
    __gtype_name__ = "BlackFennecView"
    _box = Gtk.Template.Child()

    def __init__(self, app):
        super().__init__(application=app)
        logger.info("BlackFennecView __init__")
        self._wave_button_pressed_count = 0

        self._box.add(StringViewFactory().create({}))
        self._box.add(MapViewFactory().create({}))
        self._box.show_all()

    @Gtk.Template.Callback()
    def on_button_clicked(self, info_presenter_view):
        logger.info("wave button has been pressed")
        self._wave_button_pressed_count += 1
        logger.debug("wave button click count: %i",
                     self._wave_button_pressed_count)
