import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import logging
import threading
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


    def do_startup(self):
        logger.info("BlackFennec do_startup")
        Gtk.Application.do_startup(self)

    def do_activate(self):
        logger.info("BlackFennec do_activate")
        self.set_window(SplashScreenView(self, {}))
        threading.Timer(
            1.0, self.set_window,
            args=[BlackFennecView(self)]).start()

    def set_window(self, view):
        if self._window:
            self._window.destroy()
        self._window = view
        self._window.present()



if __name__ == "__main__":
    black_fennec = BlackFennec()
    black_fennec.run()
