import pytest

from blackfennec.layers.overlay.overlay import Overlay

from blackfennec_doubles.layers.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from blackfennec_doubles.structure.double_string import StringMock
from blackfennec_doubles.structure.double_reference import ReferenceMock

@pytest.fixture
def overlay():
    return Overlay()

def test_can_construct(overlay):
    assert overlay

def test_can_apply(overlay):
    expected = StringMock()
    overlay._factory = FactoryBaseVisitorMock(returns=expected)
    structure = StringMock()
    assert overlay.apply(structure) == expected

def test_can_remember_structure(overlay):
    expected = StringMock()
    structure = StringMock()
    overlay._factory = FactoryBaseVisitorMock(returns=expected)
    assert overlay.apply(structure) == expected
    overlay._factory = FactoryBaseVisitorMock(returns=None)
    assert overlay.apply(structure) == expected

def test_does_not_remember_reference(overlay):
    expected = StringMock()
    reference = ReferenceMock()
    overlay._factory = FactoryBaseVisitorMock(returns=None)
    overlay._factory = FactoryBaseVisitorMock(returns=expected)
    assert overlay.apply(reference) is expected