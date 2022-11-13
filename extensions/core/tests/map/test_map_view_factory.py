import pytest

from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.type_system.double_type_registry import TypeRegistryMock
from blackfennec_doubles.interpretation.double_interpretation_service import InterpretationServiceMock
from blackfennec_doubles.structure.double_map import MapInstanceMock
from blackfennec.interpretation.specification import Specification
from core.map.map_view import MapView
from core.map.map_preview import MapPreview
from core.map.map_view_factory import MapViewFactory


@pytest.fixture
def factory():
    return MapViewFactory(
        InterpretationServiceMock([]),
        TypeRegistryMock(),
        Dummy('ActionRegistry'),
        Dummy('ViewFactory')
    )


def test_can_construct(factory):
    assert factory is not None


def test_can_create_map_view(factory):
    view = factory.create(
        InterpretationMock(MapInstanceMock()))
    assert isinstance(view, MapView)


def test_can_create_map_preview(factory):
    view = factory.create(InterpretationMock(
        MapInstanceMock(),
        specification=Specification(request_preview=True)))
    assert isinstance(view, MapPreview)


def test_satisfies_default(factory):
    satisfies = factory.satisfies(Specification())
    assert satisfies


def test_does_satisfy_preview(factory):
    satisfies = factory.satisfies(Specification(request_preview=True))
    assert satisfies
