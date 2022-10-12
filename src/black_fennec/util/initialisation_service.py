import logging

from src.black_fennec.document_system.document_factory import DocumentFactory
from src.black_fennec.document_system.mime_type.in_memory.in_memory_mime_type import InMemoryMimeType
from src.black_fennec.document_system.mime_type.mime_type_registry import MimeTypeRegistry
from src.black_fennec.document_system.mime_type.json.json_mime_type import JsonMimeType
from src.black_fennec.document_system.mime_type.json.json_pointer_serializer import JsonPointerSerializer
from src.black_fennec.document_system.mime_type.json.json_reference_serializer import JsonReferenceSerializer
from src.black_fennec.document_system.resource_type.protocols.bftype_resource_type import BFTypeResourceType
from src.black_fennec.structure.structure_serializer import StructureSerializer
from src.black_fennec.document_system.resource_type.protocols.file_resource_type import FileResourceType
from src.black_fennec.document_system.resource_type.protocols.https_resource_type import HttpsResourceType
from src.black_fennec.document_system.resource_type.resource_type_registry import ResourceTypeRegistry
from src.black_fennec.interpretation.auction.auctioneer import Auctioneer
from src.black_fennec.interpretation.interpretation_service import InterpretationService
from src.black_fennec.structure.type.type_loader import TypeLoader
from src.black_fennec.type_system.presenter_registry import PresenterRegistry
from src.black_fennec.type_system.type_registry import TypeRegistry
from src.extension.extension_api import ExtensionApi
from src.extension.extension_initialisation_service import ExtensionInitialisationService
from src.extension.extension_source_registry import ExtensionSourceRegistry
from src.visualisation.view_factory import ViewFactory
from src.visualisation.view_factory_registry import ViewFactoryRegistry

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


class InitialisationService():
    """BlackFennec Initialisation Service"""

    def __init__(self, extension_configuration_file: str):
        self.type_registry = TypeRegistry()
        self.resource_type_registry = ResourceTypeRegistry()
        self.mime_type_registry = MimeTypeRegistry()
        self.presenter_registry = PresenterRegistry()
        self.view_factory_registry = ViewFactoryRegistry()
        self.view_factory = ViewFactory(self.view_factory_registry)
        self.document_factory = DocumentFactory(self.resource_type_registry, self.mime_type_registry)

        self.type_loader = TypeLoader(self.document_factory, self.type_registry)
        self.extension_source_registry = ExtensionSourceRegistry()

        self.interpretation_service = InterpretationService(self.type_registry)

        self.extension_api = ExtensionApi(
            self.presenter_registry,
            self.type_registry,
            self.interpretation_service,
            self.view_factory,
            self.view_factory_registry,
            self.type_loader,
        )

        self._setup_document_system()
        self._setup_extensions(extension_configuration_file)

    def _setup_document_system(self):
        """Setup document system"""
        resource_types = [
            HttpsResourceType(),
            FileResourceType(),
            BFTypeResourceType(self.type_registry),
        ]
        for resource_type in resource_types:
            for protocol in resource_type.protocols:
                self.resource_type_registry.register_resource_type(protocol, resource_type)

        reference_parser = JsonReferenceSerializer(self.document_factory, JsonPointerSerializer)
        structure_serializer = StructureSerializer(reference_parser)

        mime_types = [
            JsonMimeType(structure_serializer),
            InMemoryMimeType(),
        ]
        for mime_type in mime_types:
            self.mime_type_registry.register_mime_type(
                mime_type.mime_type_id,
                mime_type
            )

    def _setup_extensions(self, extension_configuration_file: str):
        """Setup extensions"""
        extension_initialisation_service = ExtensionInitialisationService(self.document_factory)
        extension_initialisation_service.load_extensions_from_file(
            self.extension_source_registry,
            self.extension_api,
            extension_configuration_file
        )
