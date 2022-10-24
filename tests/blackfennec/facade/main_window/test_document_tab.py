import pytest

from blackfennec_doubles.document_system.double_document import DocumentMock
from blackfennec_doubles.document_system.double_document_factory import DocumentFactoryMock
from blackfennec_doubles.navigation.double_navigation_service import NavigationServiceMock
from blackfennec_doubles.type_system.double_presenter_registry import PresenterRegistryMock
from blackfennec_doubles.double_dummy import Dummy
from blackfennec.facade.main_window.document_tab import DocumentTab


@pytest.fixture
def presenter_registry():
    return PresenterRegistryMock()


@pytest.fixture
def document_factory():
    return DocumentFactoryMock(create_return=DocumentMock(content=Dummy()))


@pytest.fixture
def navigation_service():
    return NavigationServiceMock()


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
