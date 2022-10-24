import pytest

from doubles.black_fennec.document_system.double_document import DocumentMock
from doubles.black_fennec.document_system.double_document_factory import DocumentFactoryMock
from doubles.black_fennec.type_system.double_presenter_registry import PresenterRegistryMock
from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from doubles.extension.double_extension_source_registry import ExtensionSourceRegistryMock
from src.black_fennec.facade.extension_store.extension_store_view_model import ExtensionStoreViewModel
from src.black_fennec.facade.main_window.black_fennec_view_model import BlackFennecViewModel


@pytest.fixture()
def presenter_registry():
    return PresenterRegistryMock()


@pytest.fixture()
def interpretation_service():
    return InterpretationServiceMock(Dummy())


@pytest.fixture()
def document():
    return DocumentMock(content=Dummy())


@pytest.fixture()
def document_factory(document):
    return DocumentFactoryMock(create_return=document)


@pytest.fixture()
def extension_source_registry():
    return ExtensionSourceRegistryMock()


@pytest.fixture()
def view_model(
        presenter_registry,
        interpretation_service,
        document_factory,
        extension_source_registry,
):
    return BlackFennecViewModel(
        presenter_registry,
        interpretation_service,
        document_factory,
        Dummy(),
        extension_source_registry,
    )


def test_can_open_file(view_model, document_factory):
    view_model.open_file('/examples/black_fennec.json')


def test_can_quit_application(view_model):
    view_model.quit()


def test_can_save_file(view_model):
    view_model.save()


def test_can_save_as_file(view_model):
    view_model.save_as()


def test_can_set_project(view_model):
    view_model.set_project("test")
    assert view_model.project == "test"


def test_can_create_extension_store(view_model):
    extension_store_view_model = view_model.create_extension_store()
    assert isinstance(extension_store_view_model, ExtensionStoreViewModel)


def test_can_get_about_window_view_model(view_model):
    view_model.get_about_window_view_model()
