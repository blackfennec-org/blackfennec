import os

import gi

from src.structure.list import List
from src.util.uri.structure_encoding_service import StructureEncodingService

gi.require_version('Gtk', '3.0')

# pylint: disable=wrong-import-position,ungrouped-imports
import logging
import src.type_system
import src.presentation
from uri import URI
from gi.repository import Gtk, Gdk, GLib
from src.extension.extension_api import ExtensionApi
from src.extension.extension_source import ExtensionSource
from src.extension.local_extension_service import LocalExtensionService
from src.extension.pypi_extension_service import PyPIExtensionService
from src.interpretation.auction.auctioneer import Auctioneer
from src.interpretation.interpretation_service import InterpretationService
from src.navigation.navigation_service import NavigationService
from src.presentation.presenter_registry import PresenterRegistry
from src.type_system.type_registry import TypeRegistry
from src.util.uri.uri_import_service import UriImportService
from src.util.json.json_reference_resolving_service import JsonReferenceResolvingService
from src.util.uri.structure_parsing_service import StructureParsingService
from src.util.uri.uri_import_strategy_factory import UriImportStrategyFactory
from src.util.uri.uri_loading_strategy_factory import UriLoadingStrategyFactory
from src.visualisation.main_window.black_fennec_view_model import BlackFennecViewModel
from src.visualisation.main_window.black_fennec_view import BlackFennecView
from src.visualisation.splash_screen.splash_screen_view import SplashScreenView
# pylint: enable=wrong-import-position

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

EXTENSIONS = 'extensions.json'


def default_initialise_extensions(
        encoding_service: StructureEncodingService,
        path
):
    """
    Function creates default Extension sources
    and writes them to a file located at path

    Args:
        encoding_service (StructureEncodingService): to convert
            structure to raw json
        path (str): path of file to create
    """
    type_system = src.type_system
    type_system_source = ExtensionSource(
        LocalExtensionService(),
        identification=type_system.__name__,
        location=type_system.__path__,
        source_type='local'
    )
    for extension in type_system_source.extensions:
        extension.enabled = True

    presentation = src.presentation
    presentation_source = ExtensionSource(
        LocalExtensionService(),
        identification=presentation.__name__,
        location=presentation.__path__,
        source_type='local'
    )
    for extension in presentation_source.extensions:
        extension.enabled = True

    source_list = List([
        type_system_source.underlay,
        presentation_source.underlay
    ])

    raw = encoding_service.encode(source_list)
    file = open(path, 'w')
    file.write(raw)


def load_extensions_from_file(
        uri_import_service,
        encoding_service,
        extension_api,
        uri
):
    """
    Function loads extensions from configuration file.
    If it does not exists, it is created.

    Args:
        uri_import_service (UriImportService): used to import the config file
        encoding_service (StructureEncodingService): used to initialise file if
            it does not exists at path of uri
        extension_api (ExtensionApi): passed to loaded extensions
        uri (URI): uri of file where extension config is located
    """
    extension_services = {
        'local': LocalExtensionService(),
        'pypi': PyPIExtensionService()
    }
    absolute_path = os.path.abspath(str(uri))
    if not os.path.exists(absolute_path):
        default_initialise_extensions(encoding_service, absolute_path)

    extension_source_list = uri_import_service.load(
        uri,
        os.path.realpath(__file__)
    )
    extension_sources = list()
    for extension_source_structure in extension_source_list.children:
        source_type = extension_source_structure['type'].value
        extension_source = ExtensionSource(
            extension_services[source_type],
            extension_source_structure
        )
        extension_source.load_extensions(extension_api)
        extension_sources.append(
            extension_source
        )


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
        extension_api = ExtensionApi(
            presenter_registry,
            type_registry,
            interpretation_service
        )
        load_extensions_from_file(
            uri_import_service,
            structure_encoding_service,
            extension_api,
            URI(EXTENSIONS)
        )

        view_model = BlackFennecViewModel(
            presenter_registry.presenters[0],
            interpretation_service,
            uri_import_service
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
