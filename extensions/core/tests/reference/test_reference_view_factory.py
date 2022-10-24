import pytest

from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.structure.double_map import MapMock
from blackfennec_doubles.structure.double_reference import ReferenceInstanceMock
from blackfennec.interpretation.specification import Specification
from core.reference.reference_preview import ReferencePreview
from core.reference.reference_view_factory import ReferenceViewFactory


@pytest.fixture
def factory():
    return ReferenceViewFactory()

def test_can_construct(factory):
    assert factory is not None

def test_can_create_reference_view(factory):
    with pytest.raises(NotImplementedError):
        factory.create(InterpretationMock(MapMock()))

def test_can_create_reference_preview(factory):
    view = factory.create(
        InterpretationMock(
            ReferenceInstanceMock(reference='reference'),
            specification=Specification(request_preview=True)))
    assert isinstance(view, ReferencePreview)

def test_satisfies_default(factory):
    satisfies = factory.satisfies(Specification())
    assert satisfies == False

def test_does_satisfy_preview(factory):
    satisfies = factory.satisfies(Specification(request_preview=True))
    assert satisfies == True
