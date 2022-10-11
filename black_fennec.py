from distutils import extension
import gi

from src.black_fennec.structure.type.type_loader import TypeLoader

gi.require_version('Gtk', '3.0')

# pylint: disable=wrong-import-position,ungrouped-imports
import os
import logging
from gi.repository import Gtk, Gdk, GLib
from src.black_fennec.interpretation.interpretation_service import InterpretationService
from src.black_fennec.type_system.presenter_registry import PresenterRegistry
from src.black_fennec.type_system.type_registry import TypeRegistry
from src.black_fennec.facade.main_window.black_fennec_view_model import BlackFennecViewModel
from src.black_fennec.facade.main_window.black_fennec_view import BlackFennecView
from src.black_fennec.facade.splash_screen.splash_screen_view import SplashScreenView

from src.extension.extension_api import ExtensionApi
from src.extension.extension_initialisation_service import ExtensionInitialisationService
from src.extension.extension_source_registry import ExtensionSourceRegistry

from src.black_fennec.document_system.document_factory import DocumentFactory
from src.black_fennec.document_system.mime_type.json.json_pointer_serializer import JsonPointerSerializer
from src.black_fennec.document_system.mime_type.json.json_reference_serializer import JsonReferenceSerializer
from src.black_fennec.structure.structure_serializer import StructureSerializer
from src.black_fennec.document_system.mime_type.mime_type_registry import MimeTypeRegistry
from src.black_fennec.document_system.mime_type.json.json_mime_type import JsonMimeType
from src.black_fennec.document_system.mime_type.in_memory.in_memory_mime_type import InMemoryMimeType
from src.black_fennec.document_system.resource_type.protocols.file_resource_type import FileResourceType
from src.black_fennec.document_system.resource_type.protocols.https_resource_type import HttpsResourceType
from src.black_fennec.document_system.resource_type.protocols.bftype_resource_type import BFTypeResourceType
from src.black_fennec.document_system.resource_type.resource_type_registry import ResourceTypeRegistry

from src.visualisation.view_factory import ViewFactory
from src.visualisation.view_factory_registry import ViewFactoryRegistry

# pylint: enable=wrong-import-position

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

EXTENSIONS = os.path.realpath('extensions.json')

def create_document_factory(type_registry):
    resource_type_registry = ResourceTypeRegistry()

    resource_types = [
        HttpsResourceType(),
        FileResourceType(),
        BFTypeResourceType(type_registry),
    ]
    for resource_type in resource_types:
        for protocol in resource_type.protocols:
            resource_type_registry.register_resource_type(protocol, resource_type)

    mime_type_registry = MimeTypeRegistry()
    document_factory = DocumentFactory(resource_type_registry, mime_type_registry)

    reference_parser = JsonReferenceSerializer(document_factory, JsonPointerSerializer)

    structure_serializer = StructureSerializer(reference_parser)

    mime_types = [
        JsonMimeType(structure_serializer),
        InMemoryMimeType(),
    ]
    for mime_type in mime_types:
        mime_type_registry.register_mime_type(
            mime_type.mime_type_id,
            mime_type
        )

    return document_factory, structure_serializer

def create_extension_api(
        document_factory, type_registry, 
        presenter_registry, interpretation_service):
    view_registry = ViewFactoryRegistry()
    view_factory = ViewFactory(view_registry)
    type_loader = TypeLoader(document_factory, type_registry)

    extension_api = ExtensionApi(
        presenter_registry,
        type_registry,
        interpretation_service,
        view_factory,
        view_registry,
        type_loader
    )
    return extension_api

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
        presenter_registry = PresenterRegistry()
        interpretation_service = InterpretationService(type_registry)

        document_factory, structure_serializer = create_document_factory(type_registry)
        extension_api = create_extension_api(
            document_factory, type_registry, 
            presenter_registry, interpretation_service)
        
        extension_source_registry = ExtensionSourceRegistry()
        extension_initialisation_service = ExtensionInitialisationService(structure_serializer)
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
