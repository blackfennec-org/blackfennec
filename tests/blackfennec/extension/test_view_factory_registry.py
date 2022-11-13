import pytest

from blackfennec.extension.view_factory_registry import ViewFactoryRegistry
from blackfennec_doubles.extension.double_structure_view_factory import StructureViewFactoryMock

@pytest.fixture
def registry():
    return ViewFactoryRegistry()

@pytest.fixture
def factory():
    return StructureViewFactoryMock()

def test_can_create_view_factory_registry(registry):
    assert registry

def test_can_register_view_factory(registry, factory):
    registry.register_view_factory(None, None, factory)
    assert registry.get_factory(None, None) is factory

def test_can_deregister_view_factory(registry, factory):
    registry.register_view_factory(None, None, factory)
    registry.deregister_view_factory(None, None)
    assert registry.get_factory(None, None) is None

def test_cannot_deregister_view_factory_if_not_registered(registry, factory):
    with pytest.raises(AssertionError):
        registry.deregister_view_factory(None, None)

def test_can_get_factory_if_exists(registry, factory):
    registry.register_view_factory(None, None, factory)
    assert registry.get_factory(None, None) is factory

def test_cannot_get_factory_if_not_exists(registry, factory):
    assert registry.get_factory(None, None) is None
