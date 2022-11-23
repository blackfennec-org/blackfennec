import pytest

from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.structure.double_map import MapMock
from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.interpretation.double_specification import SpecificationMock
from base.file.file_view import FileView
from base.file.file_preview import FilePreview
from base.file.file_view_factory import FileViewFactory


@pytest.fixture
def factory():
    return FileViewFactory(Dummy("document_registry"))


def test_can_construct(factory):
    assert factory


def test_can_create_file_view(factory):
    view = factory.create(InterpretationMock(MapMock()))
    assert isinstance(view, FileView)


def test_can_create_file_preview(factory):
    view = factory.create(
        InterpretationMock(
            structure=MapMock(),
            specification=SpecificationMock(request_preview=True)))
    assert isinstance(view, FilePreview)


def test_satisfies_default(factory):
    satisfies = factory.satisfies(SpecificationMock())
    assert satisfies is True


def test_does_not_satisfy_preview(factory):
    satisfies = factory.satisfies(SpecificationMock(request_preview=True))
    assert satisfies is True
