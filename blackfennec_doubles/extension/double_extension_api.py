from blackfennec_doubles.document_system.double_document_factory import \
    DocumentFactoryMock
from blackfennec_doubles.document_system.double_document_registry import \
    DocumentRegistryMock
from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.extension.double_presenter_registry import \
    PresenterRegistryMock
from blackfennec_doubles.facade.ui_service.double_ui_service_registry import \
    UiServiceRegistryMock
from blackfennec_doubles.interpretation.double_interpretation_service import \
    InterpretationServiceMock


class ExtensionApiMock:
    def __init__(
            self,
            presenter_registry=None,
            interpretation_service=None,
            document_factory=None,
            document_registry=None,
            ui_service_registry=None,
    ):
        self.presenter_registry = presenter_registry or PresenterRegistryMock()
        self.interpretation_service = interpretation_service \
            or InterpretationServiceMock(Dummy())
        self.document_factory = document_factory or DocumentFactoryMock()
        self.document_registry = document_registry or DocumentRegistryMock()
        self.ui_service_registry = ui_service_registry or UiServiceRegistryMock()
