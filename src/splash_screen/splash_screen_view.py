import logging
from gi.repository import Gtk, Gdk

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/splash_screen/splash_screen.glade')
class SplashScreenView(Gtk.ApplicationWindow):
    """Black Fennec Splash screen"""
    __gtype_name__ = "SplashScreenView"

    def __init__(self, app, view_model):
        super().__init__(application=app)
        logger.info("SplashScreenView __init__")
        self._view_model = view_model

