import pytest

from blackfennec_doubles.document_system.double_document_registry import DocumentRegistryMock
from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.interpretation.double_specification import SpecificationMock
from blackfennec_doubles.structure.double_map import MapMock
from base.image.image_view import ImageView
from base.image.image_preview import ImagePreview
from base.image.image_view_factory import ImageViewFactory


@pytest.fixture
def factory():
    return ImageViewFactory(
        DocumentRegistryMock())


def test_can_construct(factory):
    assert factory


def test_can_create_image_view(factory):
    view = factory.create(InterpretationMock(MapMock()))
    assert isinstance(view, ImageView)


def test_can_create_image_preview(factory):
    view = factory.create(
        InterpretationMock(
            structure=MapMock(),
            specification=SpecificationMock(request_preview=True)))
    assert isinstance(view, ImagePreview)


def test_satisfies_default(factory):
    satisfies = factory.satisfies(SpecificationMock())
    assert satisfies is True


def test_does_not_satisfy_preview(factory):
    satisfies = factory.satisfies(SpecificationMock(request_preview=True))
    assert satisfies is True
