

from blackfennec_doubles.document_system.double_document_factory import DocumentFactoryMock
from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.extension.double_presenter_registry import PresenterRegistryMock
from blackfennec_doubles.facade.ui_service.double_ui_service import UiServiceMock
from blackfennec_doubles.interpretation.double_interpretation_service import InterpretationServiceMock


class ServiceLocatorMock:
    def __init__(self) -> None:
        self.presenter_registry = PresenterRegistryMock()
        self.interpretation_service = InterpretationServiceMock(Dummy())
        self.document_factory = DocumentFactoryMock()
        self.ui_service = UiServiceMock()
