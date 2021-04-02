import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
import logging
import threading
from src.black_fennec_view_model import BlackFennecViewModel
from src.black_fennec_view import BlackFennecView
from src.splash_screen.splash_screen_view import SplashScreenView

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class BlackFennec(Gtk.Application):
    def __init__(self):
        super().__init__(
            application_id="org.darwin.blackfennec")
        logger.info("BlackFennec __init__")
        self._window: Gtk.Window = None

        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        provider.load_from_path("src/style.css")
        Gtk.StyleContext.add_provider_for_screen(
            screen, provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def do_startup(self):
        logger.info("BlackFennec do_startup")
        Gtk.Application.do_startup(self)

    def do_activate(self):
        logger.info("BlackFennec do_activate")
        self.set_window(SplashScreenView(self, {}))
        
        def show_main_ui():
            view_model = BlackFennecViewModel(Gtk.Button())
            black_fennec_view = BlackFennecView(self, view_model)
            self.set_window(black_fennec_view)
        #threading.Timer(
            #0.25, show_main_ui).start()
        show_main_ui()

    def set_window(self, view):
        if self._window:
            self._window.destroy()
        self._window = view
        self._window.present()


if __name__ == "__main__":
    black_fennec = BlackFennec()
    black_fennec.run()
