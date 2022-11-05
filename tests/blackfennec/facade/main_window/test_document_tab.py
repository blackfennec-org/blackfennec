import pytest

from blackfennec_doubles.document_system.double_document import DocumentMock
from blackfennec_doubles.document_system.double_document_factory import DocumentFactoryMock
from blackfennec_doubles.document_system.mime_type.double_mime_type import MimeTypeMock
from blackfennec_doubles.document_system.resource_type.double_resource_type import ResourceTypeMock
from blackfennec_doubles.navigation.double_navigation_service import NavigationServiceMock
from blackfennec_doubles.extension.double_presenter_registry import PresenterRegistryMock
from blackfennec_doubles.double_dummy import Dummy
from blackfennec.facade.main_window.document_tab import DocumentTab
from tests.test_utils.deep_compare import DeepCompare
from tests.test_utils.parameterize import CORE_STRUCTURES


@pytest.fixture
def presenter_registry():
    return PresenterRegistryMock()


@pytest.fixture
def document():
    return DocumentMock(content=Dummy())


@pytest.fixture
def document_factory(document):
    return DocumentFactoryMock(create_return=document)


@pytest.fixture
def navigation_service():
    return NavigationServiceMock()


@pytest.fixture()
def document_tab_parametrized(request, presenter_registry, navigation_service):
    mime_type = MimeTypeMock()
    resource_type = ResourceTypeMock()
    document = DocumentMock(mime_type, resource_type, content=request.param)
    document_factory = DocumentFactoryMock(create_return=document)
    document_tab = DocumentTab(presenter_registry, document_factory, navigation_service, "uri")
    document_tab.document = document
    return document_tab


@pytest.fixture
def document_tab(presenter_registry, document_factory, navigation_service):
    return DocumentTab(presenter_registry, document_factory, navigation_service, "uri")


def test_can_construct_document_tab(document_tab):
    assert isinstance(document_tab, DocumentTab)


def test_can_create_presenter(document_tab, navigation_service):
    document_tab.create_presenter()
    assert navigation_service.set_presenter_count == 1


def test_can_load_document(document_tab, document_factory):
    document_tab.presenter = Dummy()
    document_tab.load_document()
    assert document_factory.create_count == 1


def test_can_save(document_tab, document):
    document_tab.document = document
    document_tab.save_document()
    assert document.save_count == 1


@pytest.mark.parametrize(
    "document_tab_parametrized",
    CORE_STRUCTURES,
    indirect=True,
)
def test_can_save_as(tmp_path, document_tab_parametrized: DocumentTab):
    content = document_tab_parametrized.document.content
    document_tab_parametrized.save_document_as((tmp_path / "test.json").as_posix())
    assert DeepCompare.compare(document_tab_parametrized.document.content, content)
