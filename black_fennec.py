import gi

gi.require_version('Gtk', '3.0')

# pylint: disable=wrong-import-position,ungrouped-imports
import os
import logging
from uri import URI
from gi.repository import Gtk, Gdk, GLib
from src.black_fennec.interpretation.auction.auctioneer import Auctioneer
from src.black_fennec.interpretation.interpretation_service import InterpretationService
from src.black_fennec.type_system.presenter_registry import PresenterRegistry
from src.black_fennec.type_system.type_registry import TypeRegistry
from src.black_fennec.util.uri.structure_encoding_service import StructureEncodingService
from src.black_fennec.util.uri.uri_import_service import UriImportService
from src.black_fennec.util.json.json_reference_resolving_service import JsonReferenceResolvingService
from src.black_fennec.util.uri.structure_parsing_service import StructureParsingService
from src.black_fennec.util.uri.uri_import_strategy_factory import UriImportStrategyFactory
from src.black_fennec.util.uri.uri_loading_strategy_factory import UriLoadingStrategyFactory
from src.black_fennec.facade.main_window.black_fennec_view_model import BlackFennecViewModel
from src.black_fennec.facade.main_window.black_fennec_view import BlackFennecView
from src.black_fennec.facade.splash_screen.splash_screen_view import SplashScreenView
from src.black_fennec.type_system.template_registry import TemplateRegistry

from src.extension.extension_api import ExtensionApi
from src.extension.extension_initialisation_service import ExtensionInitialisationService
from src.extension.extension_source_registry import ExtensionSourceRegistry

# pylint: enable=wrong-import-position

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

EXTENSIONS = os.path.realpath('extensions.json')


class BlackFennec(Gtk.Application):
    """BlackFennec Main Window GTK Application"""

    def __init__(self):
        super().__init__(
            application_id='org.darwin.blackfennec')
        self._window: Gtk.Window = None

        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        provider.load_from_path('src/black_fennec/facade/style.css')
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

        structure_parsing_service = StructureParsingService()
        structure_encoding_service = StructureEncodingService(indent=2)

        uri_import_strategy_factory = UriImportStrategyFactory()
        uri_loading_strategy_factory = UriLoadingStrategyFactory()
        uri_import_service = UriImportService(
            structure_parsing_service,
            uri_loading_strategy_factory,
            uri_import_strategy_factory
        )
        reference_resolving_service = \
            JsonReferenceResolvingService(uri_import_service)

        structure_parsing_service.set_reference_resolving_service(
            reference_resolving_service
        )

        presenter_registry = PresenterRegistry()
        template_registry = TemplateRegistry()
        extension_api = ExtensionApi(
            presenter_registry,
            type_registry,
            template_registry,
            interpretation_service
        )
        extension_source_registry = ExtensionSourceRegistry()
        extension_initialisation_service = ExtensionInitialisationService(structure_encoding_service)
        extension_initialisation_service.load_extensions_from_file(
            extension_source_registry,
            uri_import_service,
            extension_api,
            URI(EXTENSIONS)
        )

        view_model = BlackFennecViewModel(
            presenter_registry.presenters[0],
            interpretation_service,
            uri_import_service,
            extension_api,
            extension_source_registry
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
