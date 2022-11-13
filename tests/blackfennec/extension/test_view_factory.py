import pytest

from blackfennec_doubles.extension.double_view_factory_registry import ViewFactoryRegistryMock
from blackfennec.extension.view_factory import ViewFactory
from blackfennec_doubles.extension.double_structure_view_factory import StructureViewFactoryMock
from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.double_dummy import Dummy

@pytest.fixture
def view():
    return Dummy("view")

@pytest.fixture
def factory(view):
    return StructureViewFactoryMock(view)

@pytest.fixture
def view_factory(factory):
    registry = ViewFactoryRegistryMock(factory)
    return ViewFactory(registry)

def test_can_construct(view_factory):
    assert view_factory

def test_can_create_view(view_factory, view):
    interpretation = InterpretationMock(types=[None])
    created_view = view_factory.create(interpretation)
    assert view is created_view