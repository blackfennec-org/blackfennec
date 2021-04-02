import logging
import gi
from gi.repository import Gtk
from gi.repository import Gdk


gi.require_version("Gtk", "3.0")

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

        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        provider.load_from_path("src/style.css")
        Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


