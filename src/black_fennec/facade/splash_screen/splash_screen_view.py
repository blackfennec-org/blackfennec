import logging
from pathlib import Path
from gi.repository import Gtk, Adw

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('splash_screen.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class SplashScreenView(Adw.ApplicationWindow):
    """Black Fennec Splash screen"""
    __gtype_name__ = 'SplashScreenView'

    def __init__(self, app, view_model):
        super().__init__(application=app)
        logger.info('SplashScreenView __init__')
        self._view_model = view_model
