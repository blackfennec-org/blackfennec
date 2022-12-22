import pytest

from blackfennec_doubles.presentation_system.double_view_factory_registry import ViewFactoryRegistryMock
from blackfennec.presentation_system.structure_view_factory import StructureViewFactory
from blackfennec_doubles.presentation_system.double_structure_view_factory import StructureViewFactoryMock
from blackfennec_doubles.type_system.interpretation.double_interpretation import InterpretationMock
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
    return StructureViewFactory(registry)


def test_can_construct(view_factory):
    assert view_factory


def test_can_create_view(view_factory, view):
    interpretation = InterpretationMock(types=[None])
    created_view = next(view_factory.create(interpretation))
    assert view is created_view
