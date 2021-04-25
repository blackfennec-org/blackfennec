import gi

from src.type_system.core.reference.reference_bidder import ReferenceBidder
from src.util.file.file_import_service import FileImportService
from src.util.file.json.json_reference_resolving_service import JsonReferenceResolvingService
from src.util.file.structure_parsing_service import StructureParsingService

gi.require_version('Gtk', '3.0')

# pylint: disable=wrong-import-position
import logging
from gi.repository import Gtk, Gdk, GLib
from src.interpretation.auction.auctioneer import Auctioneer
from src.interpretation.interpretation_service import InterpretationService
from src.navigation.navigation_service import NavigationService
from src.presentation.column_based_presenter.column_based_presenter_view_factory import ColumnBasedPresenterViewFactory
from src.type_system.type_registry import TypeRegistry
from src.type_system.base.address.address_bidder import AddressBidder
from src.type_system.base.date_time.date_time_bidder import DateTimeBidder
from src.type_system.base.file.file_bidder import FileBidder
from src.type_system.base.image.image_bidder import ImageBidder
from src.type_system.base.person.person_bidder import PersonBidder
from src.type_system.core.boolean.boolean_bidder import BooleanBidder
from src.type_system.core.list.list_bidder import ListBidder
from src.type_system.core.map.map_bidder import MapBidder
from src.type_system.core.number.number_bidder import NumberBidder
from src.type_system.core.string.string_bidder import StringBidder
from src.visualisation.main_window.black_fennec_view_model import BlackFennecViewModel
from src.visualisation.main_window.black_fennec_view import BlackFennecView
from src.visualisation.splash_screen.splash_screen_view import SplashScreenView
# pylint: enable=wrong-import-position

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def populate_type_registry(
        registry: TypeRegistry,
        interpretation_service: InterpretationService):
    """
    Function populates type registry. Used
    as a mock before the ExtensionManager makes
    this function obsolete.

    Args:
        registry (TypeRegistry): type registry on which to register types
        interpretation_service (InterpretationService): interpretation service
            required by map to be able to show previews.
    """
    registry.register_type(BooleanBidder())
    registry.register_type(NumberBidder())
    registry.register_type(StringBidder())
    registry.register_type(ListBidder())
    registry.register_type(MapBidder(interpretation_service))
    registry.register_type(ReferenceBidder(interpretation_service))
    registry.register_type(FileBidder())
    registry.register_type(ImageBidder())
    registry.register_type(AddressBidder())
    registry.register_type(DateTimeBidder())
    registry.register_type(PersonBidder())


class BlackFennec(Gtk.Application):
    """BlackFennec Main Window GTK Application"""
    def __init__(self):
        super().__init__(
            application_id='org.darwin.blackfennec')
        self._window: Gtk.Window = None

        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        provider.load_from_path('src/visualisation/style.css')
        Gtk.StyleContext.add_provider_for_screen(
            screen, provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        self.set_window(SplashScreenView(self, {}))
        GLib.timeout_add(100, self.do_setup)

    def do_setup(self):
        """Setup BlackFennec application"""
        logger.debug('do_setup')
        type_registry = TypeRegistry()
        auctioneer = Auctioneer(type_registry)
        interpretation_service = InterpretationService(auctioneer)
        navigation_service = NavigationService()
        structure_parsing_service = StructureParsingService()
        file_import_service = FileImportService(structure_parsing_service)
        reference_resolving_service = JsonReferenceResolvingService(file_import_service)
        structure_parsing_service.set_reference_resolving_service(reference_resolving_service)
        presenter_view = ColumnBasedPresenterViewFactory() \
            .create(interpretation_service, navigation_service)
        presenter = presenter_view._view_model # pylint: disable=protected-access
        navigation_service.set_presenter(presenter)
        populate_type_registry(type_registry, interpretation_service)
        view_model = BlackFennecViewModel(
            presenter_view,
            navigation_service,
            file_import_service
        )
        black_fennec_view = BlackFennecView(self, view_model)
        logger.debug('show_main_ui')
        self.set_window(black_fennec_view)
        return False

    def set_window(self, view):
        if self._window:
            self._window.destroy()
        self._window = view
        self._window.present()


if __name__ == '__main__':
    black_fennec = BlackFennec()
    black_fennec.run()
