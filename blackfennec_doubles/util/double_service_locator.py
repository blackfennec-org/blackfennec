

from blackfennec_doubles.document_system.double_document_factory import DocumentFactoryMock
from blackfennec_doubles.document_system.mime_type.double_mime_type_registry import \
    MimeTypeRegistryMock
from blackfennec_doubles.document_system.resource_type.double_resource_type_registry import \
    ResourceTypeRegistryMock
from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.presentation_system.double_presenter_registry import PresenterRegistryMock
from blackfennec_doubles.presentation_system.ui_service.double_ui_service import UiServiceMock
from blackfennec_doubles.type_system.interpretation.double_interpretation_service import InterpretationServiceMock


class ServiceLocatorMock:
    def __init__(self) -> None:
        self.presenter_registry = PresenterRegistryMock()
        self.interpretation_service = InterpretationServiceMock(Dummy())
        self.document_factory = DocumentFactoryMock()
        self.ui_service = UiServiceMock()
        self.resource_type_registry = ResourceTypeRegistryMock()
        self.mime_type_registry = MimeTypeRegistryMock()
