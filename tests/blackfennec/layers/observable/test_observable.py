import pytest

from blackfennec.layers.observable.observable import ObservableLayer

from blackfennec_doubles.structure.double_string import StringMock
from blackfennec_doubles.layers.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock

@pytest.fixture
def layer():
    return ObservableLayer()

def test_can_construct(layer):
    assert layer

def test_can_apply(layer):
    expected = StringMock()
    layer._factory = FactoryBaseVisitorMock(returns=expected)
    structure = StringMock()
    assert layer.apply(structure) == expected

def test_can_remember_structure(layer):
    expected = StringMock()
    structure = StringMock()
    layer._factory = FactoryBaseVisitorMock(returns=expected)
    assert layer.apply(structure) == expected
    layer._factory = FactoryBaseVisitorMock(returns=None)
    assert layer.apply(structure) == expected
