from blackfennec_doubles.document_system.double_document_factory import \
    DocumentFactoryMock
from blackfennec_doubles.extension.double_presenter_registry import \
    PresenterRegistryMock
from blackfennec_doubles.interpretation.double_interpretation_service import \
    InterpretationServiceMock
from doubles.double_dummy import Dummy


class ExtensionApiMock:
    def __init__(
            self,
            presenter_registry=None,
            interpretation_service=None,
            document_factory=None,
    ):
        self.presenter_registry = presenter_registry or PresenterRegistryMock()
        self.interpretation_service = interpretation_service \
            or InterpretationServiceMock(Dummy())
        self.document_factory = document_factory or DocumentFactoryMock()
