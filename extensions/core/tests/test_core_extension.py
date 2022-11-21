import pytest
from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.extension.double_view_factory_registry import \
    ViewFactoryRegistryMock
from blackfennec_doubles.extension.double_presenter_registry import \
    PresenterRegistryMock
from blackfennec_doubles.type_system.double_type_registry import \
    TypeRegistryMock
from blackfennec_doubles.actions.double_action_registry import \
    ActionRegistryMock

from blackfennec.extension.extension_api import ExtensionApi
from core import create_extension, destroy_extension


@pytest.fixture
def type_registry() -> TypeRegistryMock:
    return TypeRegistryMock()


@pytest.fixture
def presenter_registry() -> PresenterRegistryMock:
    return PresenterRegistryMock()


@pytest.fixture
def extension_api(type_registry, presenter_registry) -> ExtensionApi:
    return ExtensionApi(
        presenter_registry=presenter_registry,
        type_registry=type_registry,
        interpretation_service=Dummy("InterpretationService"),
        view_factory=Dummy("ViewFactory"),
        view_factory_registry=ViewFactoryRegistryMock(),
        type_loader=Dummy("TypeLoader"),
        action_registry=ActionRegistryMock(),
    )


def test_create_core_extension(extension_api, type_registry,
                               presenter_registry):
    create_extension(extension_api)
    assert type_registry.register_type_count == 7
    assert presenter_registry.register_presenter_count == 1


def test_destroy_core_extension(extension_api, type_registry,
                                presenter_registry):
    destroy_extension(extension_api)
    assert type_registry.deregister_type_count == 7
    assert presenter_registry.deregister_presenter_count == 1


def test_everything_created_is_destroyed(extension_api, type_registry,
                                         presenter_registry):
    create_extension(extension_api)
    destroy_extension(extension_api)
    assert type_registry.register_type_count == \
           type_registry.deregister_type_count
    assert presenter_registry.register_presenter_count == \
           presenter_registry.deregister_presenter_count
