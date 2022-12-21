import pytest

from blackfennec.presentation_system.main_window.black_fennec_view_model import \
    BlackFennecViewModel
from blackfennec_doubles.document_system.double_document import DocumentMock
from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.extension.double_extension_source_registry import \
    ExtensionSourceRegistryMock
from blackfennec_doubles.extension.double_presenter_registry import \
    PresenterRegistryMock
from blackfennec_doubles.presentation_system.main_window.double_document_tab import \
    DocumentTabMock
from blackfennec_doubles.interpretation.double_interpretation_service import InterpretationServiceMock
from blackfennec_doubles.extension.double_extension_source_registry import ExtensionSourceRegistryMock
from blackfennec.presentation_system.main_window.black_fennec_view_model import BlackFennecViewModel
from blackfennec_doubles.util.double_service_locator import ServiceLocatorMock


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
def document_tab(document):
    return DocumentTabMock(document)


@pytest.fixture
def service_locator():
    return ServiceLocatorMock()


@pytest.fixture()
def extension_source_registry():
    return ExtensionSourceRegistryMock()


@pytest.fixture()
def view_model(service_locator):
    view_model = BlackFennecViewModel(service_locator)
    return view_model


@pytest.mark.parametrize('file_path', [
    'test.json',
    '/'
])
def test_can_open(file_path, view_model):
    view_model.open(file_path)


def test_can_open_file(view_model):
    view_model.open_file('/examples/black_fennec.json')


def test_can_handle_uri(view_model, service_locator):
    service_locator.resource_type_registry.resource_types = {
        'file': Dummy()
    }
    service_locator.mime_type_registry.mime_types = {
        'application/json': Dummy()
    }
    assert view_model.can_handle_uri('/examples/black_fennec.json')


def test_cannot_handle_uri(view_model):
    assert not view_model.can_handle_uri('test')


def test_can_save_file(view_model, document_tab):
    view_model.save(document_tab)
    assert document_tab.save_document_count == 1


def test_can_save_as_file(view_model, document_tab, tmp_path):
    view_model.save_as(document_tab, (tmp_path / 'test.json').as_posix())
    assert document_tab.save_document_as_count == 1


def test_save_all(view_model, document_tab):
    view_model.tabs = [document_tab]
    view_model.save_all()
    assert document_tab.save_document_count == 1


def test_can_close_file(view_model, document_tab):
    view_model.tabs = [document_tab]
    view_model.close_file(document_tab)
    assert view_model.tabs == []


def test_can_undo(view_model, document_tab):
    document_tab.history.append(Dummy())
    view_model.undo(document_tab)
    assert document_tab.history.undo_count == 1


def test_cannot_undo(view_model, document_tab):
    with pytest.raises(ValueError):
        view_model.undo(document_tab)


def test_can_redo(view_model, document_tab):
    document_tab.history.append(Dummy())
    view_model.redo(document_tab)
    assert document_tab.history.redo_count == 1


def test_cannot_redo(view_model, document_tab):
    with pytest.raises(ValueError):
        view_model.redo(document_tab)


def test_can_set_directory(view_model):
    view_model.current_directory = 'test'
    assert view_model.current_directory == 'test'


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
