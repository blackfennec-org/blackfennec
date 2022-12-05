import logging

from blackfennec.document_system.document_factory import DocumentFactory
from blackfennec.document_system.document_registry import DocumentRegistry
from blackfennec.document_system.mime_type.in_memory.in_memory_mime_type import \
    InMemoryMimeType
from blackfennec.document_system.mime_type.mime_type_registry import \
    MimeTypeRegistry
from blackfennec.document_system.mime_type.json.json_mime_type import \
    JsonMimeType
from blackfennec.document_system.mime_type.json.json_pointer_serializer import \
    JsonPointerSerializer
from blackfennec.document_system.mime_type.json.json_reference_serializer import \
    JsonReferenceSerializer
from blackfennec.document_system.resource_type.protocols.bftype_resource_type import \
    BFTypeResourceType
from blackfennec.facade.ui_service.ui_service_registry import UiServiceRegistry
from blackfennec.structure.structure_serializer import StructureSerializer
from blackfennec.document_system.resource_type.protocols.file_resource_type import \
    FileResourceType
from blackfennec.document_system.resource_type.protocols.https_resource_type import \
    HttpsResourceType
from blackfennec.document_system.resource_type.resource_type_registry import \
    ResourceTypeRegistry
from blackfennec.interpretation.interpretation_service import \
    InterpretationService
from blackfennec.type_system.type_loader import TypeLoader
from blackfennec.extension.presenter_registry import PresenterRegistry
from blackfennec.type_system.type_registry import TypeRegistry
from blackfennec.actions.action_registry import ActionRegistry
from blackfennec.extension.extension_api import ExtensionApi
from blackfennec.extension.extension_initialisation_service import \
    ExtensionInitialisationService
from blackfennec.extension.extension_source_registry import \
    ExtensionSourceRegistry
from blackfennec.extension.view_factory import ViewFactory
from blackfennec.extension.view_factory_registry import ViewFactoryRegistry

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
        self.action_registry = ActionRegistry()
        self.view_factory = ViewFactory(self.view_factory_registry)

        self.document_registry = DocumentRegistry()
        self.document_factory = DocumentFactory(
            self.document_registry,
            self.resource_type_registry,
            self.mime_type_registry)

        self.type_loader = TypeLoader(
            self.document_factory, self.type_registry)
        self.extension_source_registry = ExtensionSourceRegistry()

        self.interpretation_service = InterpretationService(self.type_registry)

        self.ui_service_registry = UiServiceRegistry()

        self.extension_api = ExtensionApi(
            self.presenter_registry,
            self.type_registry,
            self.interpretation_service,
            self.view_factory,
            self.view_factory_registry,
            self.type_loader,
            self.action_registry,
            self.document_registry,
            self.document_factory,
            self.ui_service_registry,
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
                self.resource_type_registry.register_resource_type(
                    protocol, resource_type)

        reference_parser = JsonReferenceSerializer(
            self.document_factory, JsonPointerSerializer)
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
        extension_initialisation_service = ExtensionInitialisationService(
            self.document_factory)
        extension_initialisation_service.load_extensions_from_file(
            self.extension_source_registry,
            self.extension_api,
            extension_configuration_file
        )
