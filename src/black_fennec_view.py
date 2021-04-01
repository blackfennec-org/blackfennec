import logging
from gi.repository import Gtk
from src.core.string import StringViewFactory
from src.core.map import MapViewFactory

logger = logging.getLogger(__name__)

@Gtk.Template(filename="src/black_fennec.glade")
class BlackFennecView(Gtk.ApplicationWindow):
    __gtype_name__ = "BlackFennecView"
    _presenter_container = Gtk.Template.Child()

    def __init__(self, app, view_model):
        super().__init__(application=app)
        logger.info("BlackFennecView __init__")
        self._view_model = view_model
        self._presenter_container.add(self._view_model.presenter)
        self._presenter_container.show_all()


