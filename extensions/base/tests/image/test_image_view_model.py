import pytest

from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.structure.double_map import MapMock
from blackfennec_doubles.structure.double_string import StringMock
from blackfennec_doubles.document_system.double_document_registry import DocumentRegistryMock
from base.image.image import Image
from base.image.image_view_model import ImageViewModel


@pytest.fixture
def map():
    data = {
        Image.FILE_PATH_KEY: StringMock('file_path'),
        Image.FILE_TYPE_KEY: StringMock('file_type')
    }
    return MapMock(data)


@pytest.fixture
def interpretation(map):
    return InterpretationMock(map)


@pytest.fixture
def view_model(interpretation):
    registry = DocumentRegistryMock()
    return ImageViewModel(interpretation, registry)


def test_can_construct(view_model):
    assert view_model


def test_can_get_file_path(view_model):
    assert view_model.file_path == 'file_path'


def test_can_set_file_path(view_model):
    file_path = '/path/to/file'
    view_model.file_path = file_path
    assert view_model.file_path == file_path


def test_can_get_file_type(view_model):
    assert view_model.file_type == 'file_type'


def test_can_set_file_type(view_model):
    file_type = 'image/png'
    view_model.file_type = file_type
    assert view_model.file_type == file_type


def test_can_get_absolute_path(view_model):
    assert view_model.absolute_path == '/home/blackfennec/file_path'


def test_can_get_already_absolute_path(view_model):
    view_model.file_path = '/path/to/file'
    assert view_model.absolute_path == '/path/to/file'


def test_can_set_absolute_path(view_model):
    absolute_path = '/home/blackfennec/path/to/file'
    view_model.absolute_path = absolute_path
    assert view_model.absolute_path == absolute_path
    assert view_model.file_path == 'path/to/file'


def test_can_set_random_absolute_path(view_model):
    absolute_path = '/path/to/file'
    view_model.absolute_path = absolute_path
    assert view_model.absolute_path == absolute_path
    assert view_model.file_path == '/path/to/file'


def test_can_get_location(view_model):
    assert view_model.location == '/home/blackfennec'


def test_can_navigate(view_model, interpretation):
    view_model.navigate()
    assert len(interpretation.navigation_requests) == 1
