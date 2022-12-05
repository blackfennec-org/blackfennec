import pytest

from blackfennec.facade.extension_store.extension_store_view_model import \
    ExtensionStoreViewModel
from blackfennec.facade.main_window.black_fennec_view_model import \
    BlackFennecViewModel
from blackfennec_doubles.document_system.double_document import DocumentMock
from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.extension.double_extension_api import ExtensionApiMock
from blackfennec_doubles.extension.double_extension_source_registry import \
    ExtensionSourceRegistryMock
from blackfennec_doubles.facade.main_window.double_document_tab import \
    DocumentTabMock
from blackfennec_doubles.facade.ui_service.double_ui_service import \
    UiServiceMock
from blackfennec_doubles.facade.ui_service.double_ui_service_registry import \
    UiServiceRegistryMock


@pytest.fixture()
def document():
    return DocumentMock(content=Dummy())


@pytest.fixture()
def document_tab(document):
    return DocumentTabMock(document)


@pytest.fixture()
def ui_service():
    return UiServiceMock()


@pytest.fixture()
def ui_service_key():
    return Dummy('ui_service_key')


@pytest.fixture
def extension_api(ui_service, ui_service_key):
    return ExtensionApiMock(
        ui_service_registry=UiServiceRegistryMock(
            ui_service=ui_service,
            ui_service_key=ui_service_key
        ),
    )


@pytest.fixture()
def extension_source_registry():
    return ExtensionSourceRegistryMock()


@pytest.fixture()
def view_model(
        extension_api,
        extension_source_registry,
        ui_service,
        ui_service_key,
):
    view_model = BlackFennecViewModel(
        extension_api,
        extension_source_registry,
    )
    view_model.set_ui_service(ui_service_key, ui_service)
    return view_model


def test_can_open_file(view_model):
    view_model.open_file('/examples/black_fennec.json')


def test_can_save_file(view_model, document_tab):
    view_model.save(document_tab)
    assert document_tab.save_document_count == 1


def test_can_save_as_file(view_model, document_tab, tmp_path):
    view_model.save_as(document_tab, (tmp_path / "test.json").as_posix())
    assert document_tab.save_document_as_count == 1


def test_can_set_directory(view_model):
    view_model.current_directory = "test"
    assert view_model.current_directory == "test"


def test_can_create_extension_store(view_model):
    extension_store_view_model = view_model.create_extension_store()
    assert isinstance(extension_store_view_model, ExtensionStoreViewModel)


def test_can_get_about_window_view_model(view_model):
    view_model.get_about_window_view_model()


def test_can_copy_view_model(view_model):
    view_model_copy = view_model.copy()
    assert isinstance(view_model_copy, BlackFennecViewModel)


def test_can_attach_tab(view_model):
    tab = Dummy()
    view_model.attach_tab(tab)
    assert tab in view_model.tabs


def test_can_detach_tab(view_model):
    tab = Dummy()
    view_model.tabs = [tab]
    view_model.detach_tab(tab)
    assert tab not in view_model.tabs
