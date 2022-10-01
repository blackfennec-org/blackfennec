import pytest

from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.structure.double_number import NumberMock
from src.black_fennec.interpretation.specification import Specification
from src.visualisation.core.number.number_preview import NumberPreview
from src.visualisation.core.number.number_view import NumberView
from src.visualisation.core.number.number_view_factory import NumberViewFactory


@pytest.fixture
def factory():
    return NumberViewFactory()

def test_can_construct(factory):
    assert factory is not None

def test_can_create_number_view(factory):
    view = factory.create(
        InterpretationMock(NumberMock()))
    assert isinstance(view, NumberView)

def test_can_create_string_preview(factory):
    specification = Specification(request_preview=True)
    view = factory.create(
        InterpretationMock(NumberMock(), 
        specification=specification))
    assert isinstance(view, NumberPreview)

def test_satisfies_default(factory):
    satisfies = factory.satisfies(Specification())
    assert satisfies

def test_does_satisfy_preview(factory):
    satisfies = factory.satisfies(Specification(request_preview=True))
    assert satisfies
