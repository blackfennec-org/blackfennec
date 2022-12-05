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
from tests.test_utils.observer import Observer


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


def test_can_set_ui_service_second_time(view_model, ui_service, ui_service_key):
    with pytest.raises(AssertionError):
        view_model.set_ui_service(ui_service_key, ui_service)


def test_can_get_ui_service(view_model, ui_service_key, ui_service):
    assert view_model.get_ui_service(ui_service_key) is ui_service


def test_can_save_file(view_model, document_tab):
    view_model.save(document_tab)
    assert document_tab.save_document_count == 1


def test_can_save_as_file(view_model, document_tab, tmp_path):
    view_model.save_as(document_tab, (tmp_path / "test.json").as_posix())
    assert document_tab.save_document_as_count == 1


def test_save_all(view_model, document_tab, ui_service):
    view_model.tabs = [document_tab]
    view_model.save_all()
    assert document_tab.save_document_count == 1
    assert ui_service.show_message_count == 2


def test_can_close_file(view_model, document_tab, ui_service):
    view_model.tabs = [document_tab]
    view_model.close_file(document_tab)
    assert view_model.tabs == []
    assert ui_service.show_message_count == 1


def test_can_undo(view_model, document_tab, ui_service):
    document_tab.history.append(Dummy())
    view_model.undo(document_tab)
    assert document_tab.history.undo_count == 1
    assert ui_service.show_message_count == 1


def test_cannot_undo(view_model, ui_service, document_tab):
    view_model.undo(document_tab)
    assert document_tab.history.undo_count == 0
    assert ui_service.show_message_count == 1


def test_can_redo(view_model, document_tab, ui_service):
    document_tab.history.append(Dummy())
    view_model.redo(document_tab)
    assert document_tab.history.redo_count == 1
    assert ui_service.show_message_count == 1


def test_cannot_redo(view_model, ui_service, document_tab):
    view_model.redo(document_tab)
    assert document_tab.history.redo_count == 0
    assert ui_service.show_message_count == 1


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


def test_cannot_attach_tab_twice(view_model):
    tab = Dummy()
    view_model.attach_tab(tab)
    with pytest.raises(AssertionError):
        view_model.attach_tab(tab)


def test_can_detach_tab(view_model):
    tab = Dummy()
    view_model.tabs = [tab]
    view_model.detach_tab(tab)
    assert tab not in view_model.tabs


def test_cannot_detach_tab_which_is_not_attached(view_model):
    tab = Dummy()
    with pytest.raises(AssertionError):
        view_model.detach_tab(tab)

def test_dispatch_message(view_model, ui_service):
    sender = Dummy('sender')
    message = Dummy('message')
    observer = Observer()
    view_model.bind(message=observer.endpoint)
    view_model._dispatch_message(sender, message)
    assert observer.last_call[0][0] == sender
    assert observer.last_call[0][1] == message
