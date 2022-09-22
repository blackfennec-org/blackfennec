import gi

gi.require_version('Gtk', '3.0')

# pylint: disable=wrong-import-position,ungrouped-imports
import os
import logging
from gi.repository import Gtk, Gdk, GLib
from src.black_fennec.interpretation.auction.auctioneer import Auctioneer
from src.black_fennec.interpretation.interpretation_service import InterpretationService
from src.black_fennec.type_system.presenter_registry import PresenterRegistry
from src.black_fennec.type_system.type_registry import TypeRegistry
from src.black_fennec.util.json.json_reference_resolving_service import JsonReferenceResolvingService
from src.black_fennec.facade.main_window.black_fennec_view_model import BlackFennecViewModel
from src.black_fennec.facade.main_window.black_fennec_view import BlackFennecView
from src.black_fennec.facade.splash_screen.splash_screen_view import SplashScreenView
from src.black_fennec.type_system.type_registry import TypeRegistry

from src.extension.extension_api import ExtensionApi
from src.extension.extension_initialisation_service import ExtensionInitialisationService
from src.extension.extension_source_registry import ExtensionSourceRegistry

from src.black_fennec.util.document.mime_type.types.structure_parsing_service import StructureParsingService
from src.black_fennec.util.document.mime_type.types.structure_encoding_service import StructureEncodingService
from src.black_fennec.util.document.mime_type.mime_type_registry import MimeTypeRegistry
from src.black_fennec.util.document.mime_type.types.json.json_mime_type import JsonMimeType
from src.black_fennec.util.document.resource_type.protocols.file_resource_type import FileResourceType
from src.black_fennec.util.document.resource_type.protocols.https_resource_type import HttpsResourceType
from src.black_fennec.util.document.resource_type.resource_type_registry import ResourceTypeRegistry
from src.black_fennec.util.document.document_factory import DocumentFactory

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

        resource_type_registry = ResourceTypeRegistry()
        for protocol in HttpsResourceType.PROTOCOLS:
            resource_type_registry.register_resource_type(protocol, HttpsResourceType())
        for protocol in FileResourceType.PROTOCOLS:
            resource_type_registry.register_resource_type(protocol, FileResourceType())

        mime_type_registry = MimeTypeRegistry()
        mime_type_registry.register_mime_type(
            JsonMimeType.MIME_TYPE_ID,
            JsonMimeType(
                structure_encoding_service,
                structure_parsing_service
            )
        )

        document_factory = DocumentFactory(resource_type_registry, mime_type_registry)

        reference_resolving_service = \
            JsonReferenceResolvingService(document_factory)

        structure_parsing_service.set_reference_resolving_service(
            reference_resolving_service
        )

        presenter_registry = PresenterRegistry()
        type_registry = TypeRegistry()
        extension_api = ExtensionApi(
            presenter_registry,
            type_registry,
            type_registry,
            interpretation_service
        )
        extension_source_registry = ExtensionSourceRegistry()
        extension_initialisation_service = ExtensionInitialisationService(structure_encoding_service)
        extension_initialisation_service.load_extensions_from_file(
            extension_source_registry,
            document_factory,
            extension_api,
            EXTENSIONS
        )

        view_model = BlackFennecViewModel(
            presenter_registry.presenters[0],
            interpretation_service,
            document_factory,
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
