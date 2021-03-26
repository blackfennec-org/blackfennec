import logging
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from src.black_fennec_view import BlackFennecView

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class BlackFennec(Gtk.Application):
    def __init__(self):
        super().__init__(
            application_id="org.darwin.blackfennec")
        logger.info("BlackFennec __init__")
        self._window = None

    def do_startup(self):
        logger.info("BlackFennec do_startup")
        Gtk.Application.do_startup(self)

    def do_activate(self):
        logger.info("BlackFennec do_activate")
        self._window = BlackFennecView(self)
        self._window.present()


if __name__ == "__main__":
    black_fennec = BlackFennec()
    black_fennec.run()
