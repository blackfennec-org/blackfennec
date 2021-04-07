import gi
gi.require_version('Gtk', '3.0')

# pylint: disable=wrong-import-position
import logging
import threading
from gi.repository import Gtk, Gdk
from src.black_fennec_view_model import BlackFennecViewModel
from src.black_fennec_view import BlackFennecView
from src.extension.type_registry import TypeRegistry
from src.core.boolean.boolean_bidder import BooleanBidder
from src.core.number.number_bidder import NumberBidder
from src.core.string.string_bidder import StringBidder
from src.core.list.list_bidder import ListBidder
from src.core.map.map_bidder import MapBidder
from src.core import Auctioneer, NavigationService
from src.base.column_based_presenter import ColumnBasedPresenterViewFactory
from src.splash_screen.splash_screen_view import SplashScreenView
# pylint: enable=wrong-import-position

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_type_registry() -> TypeRegistry:
    registry = TypeRegistry()
    registry.register_type(BooleanBidder())
    registry.register_type(NumberBidder())
    registry.register_type(StringBidder())
    registry.register_type(ListBidder())
    registry.register_type(MapBidder())
    return registry

class BlackFennec(Gtk.Application):
    def __init__(self, presenter_view, navigation_service):
        super().__init__(
            application_id='org.darwin.blackfennec')
        logger.info('BlackFennec __init__')
        self._window: Gtk.Window = None
        self._presenter_view = presenter_view
        self._navigation_service = navigation_service

        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        provider.load_from_path('src/style.css')
        Gtk.StyleContext.add_provider_for_screen(
            screen, provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def do_startup(self):
        logger.info('BlackFennec do_startup')
        Gtk.Application.do_startup(self)

    def do_activate(self):
        logger.info('BlackFennec do_activate')
        self.set_window(SplashScreenView(self, {}))

        def show_main_ui():
            view_model = BlackFennecViewModel(
                self._presenter_view,
                self._navigation_service)
            black_fennec_view = BlackFennecView(self, view_model)
            self.set_window(black_fennec_view)

        threading.Timer(
            0.25, show_main_ui).start()

    def set_window(self, view):
        if self._window:
            self._window.destroy()
        self._window = view
        self._window.present()


if __name__ == '__main__':
    presenter_view = ColumnBasedPresenterViewFactory().create()
    presenter = presenter_view._view_model
    type_registry = create_type_registry()
    auctioneer = Auctioneer(type_registry)
    navigation_service = NavigationService(presenter, auctioneer)
    black_fennec = BlackFennec(presenter_view, navigation_service)
    black_fennec.run()
