import logging
import os
import sys

from blackfennec.facade.main_window.black_fennec_view import BlackFennecView
from blackfennec.facade.main_window.black_fennec_view_model import \
    BlackFennecViewModel
from blackfennec.facade.splash_screen.splash_screen_view import SplashScreenView
from blackfennec.util.initialisation_service import InitialisationService

from gi.repository import Adw, Gio, Gtk

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

CONFIG_HOME = os.path.expanduser('~/.config/blackfennec/')
if not os.path.exists(CONFIG_HOME):
    os.makedirs(CONFIG_HOME)
EXTENSIONS = os.path.join(CONFIG_HOME, os.path.relpath('extensions.json'))


class BlackFennec(Adw.Application):
    """BlackFennec GTK Application"""

    def __init__(self, initialisation_service: InitialisationService):
        super().__init__(
            application_id='org.blackfennec.app',
            flags=Gio.ApplicationFlags.FLAGS_NONE
        )
        self._initialisation_service = initialisation_service

    def do_activate(self):
        win = self.props.active_window
        if not win:
            splash_screen = SplashScreenView(self, {})
            splash_screen.present()
            win = self.do_setup()
            splash_screen.destroy()
        win.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)

    def do_setup(self):
        """Setup BlackFennec application"""

        view_model = BlackFennecViewModel(
            self._initialisation_service.extension_api,
        )
        black_fennec_view = BlackFennecView(self, view_model)
        return black_fennec_view


if __name__ == '__main__':
    initialisation_service = InitialisationService(
        extension_configuration_file=EXTENSIONS
    )
    black_fennec = BlackFennec(initialisation_service)
    black_fennec.run(sys.argv)
