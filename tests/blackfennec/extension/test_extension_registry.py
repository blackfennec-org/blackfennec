import pytest

from blackfennec_doubles.double_dummy import Dummy
from blackfennec.extension.extension_registry import ExtensionRegistry

@pytest.fixture
def extension_registry():
    return ExtensionRegistry()

def can_construct(extension_registry):
    assert extension_registry

def can_register_extension(extension_registry):
    extension = Dummy('Extension')
    extension_registry.register_extension(extension)
    assert extension_registry.get_extensions() == [extension]
