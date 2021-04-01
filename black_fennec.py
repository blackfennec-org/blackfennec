import logging
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from src.black_fennec_view_model import BlackFennecViewModel
from src.black_fennec_view import BlackFennecView
from src.extension.type_registry import TypeRegistry
from src.core import BooleanBidder, BooleanViewFactory, \
        Number, NumberBidder, NumberViewFactory, \
        String, StringBidder, StringViewFactory, \
        List, ListBidder, ListViewFactory, \
        Map, MapBidder, MapViewFactory, \
        Info, Auctioneer, NavigationService
from src.base.column_based_presenter import ColumnBasedPresenterViewFactory

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_type_registry() -> TypeRegistry:
    registry = TypeRegistry()
    registry.register_type(BooleanBidder(), BooleanViewFactory())
    registry.register_type(NumberBidder(), NumberViewFactory())
    registry.register_type(StringBidder(), StringViewFactory())
    registry.register_type(ListBidder(), ListViewFactory())
    registry.register_type(MapBidder(), MapViewFactory())
    return registry

def create_structure() -> Info:
    structure = Map({
        "Team": List([
            Map({
                "name": String("Leonie")
            }),
            Map({
                "name": String("Lara")
            }),
            Map({
                "name": String("Caspar")
            }),
            Map({
                "name": String("Simon")
            })
        ]),
        "Repository": String(
            "https://gitlab.ost.ch/epj/2021-FS/g01_blackfennec/black-fennec")
    })
    return structure

class BlackFennec(Gtk.Application):
    def __init__(self, presenter_view):
        super().__init__(
            application_id="org.darwin.blackfennec")
        logger.info("BlackFennec __init__")
        self._presenter_view = presenter_view
        self._window = None

    def do_startup(self):
        logger.info("BlackFennec do_startup")
        Gtk.Application.do_startup(self)

    def do_activate(self):
        logger.info("BlackFennec do_activate")
        view_model = BlackFennecViewModel(self._presenter_view)
        self._window = BlackFennecView(self, view_model)
        self._window.present()


if __name__ == "__main__":
    presenter_view = ColumnBasedPresenterViewFactory().create()
    presenter = presenter_view._view_model
    type_registry = create_type_registry()
    auctioneer = Auctioneer(type_registry)
    navigation_service = NavigationService(presenter, auctioneer)
    structure = create_structure()
    navigation_service.navigate(None, structure)
    black_fennec = BlackFennec(presenter_view)
    black_fennec.run()
