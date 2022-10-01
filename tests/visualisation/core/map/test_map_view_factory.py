import pytest

from doubles.double_dummy import Dummy
from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.type_system.double_template_registry import TemplateRegistryMock
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from doubles.black_fennec.structure.double_map import MapInstanceMock
from src.black_fennec.interpretation.specification import Specification
from src.visualisation.core.map.map_view import MapView
from src.visualisation.core.map.map_preview import MapPreview
from src.visualisation.core.map.map_view_factory import MapViewFactory


@pytest.fixture
def factory():
    return MapViewFactory(
        InterpretationServiceMock([]),
        TemplateRegistryMock(),
        Dummy('ViewFactory'))


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
