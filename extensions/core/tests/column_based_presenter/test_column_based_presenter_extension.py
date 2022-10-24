import pytest

from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.type_system.double_presenter_registry import PresenterRegistryMock
from blackfennec.extension.extension_api import ExtensionApi
from core.column_based_presenter import create_extension, destroy_extension


@pytest.fixture
def registry() -> PresenterRegistryMock:
    return PresenterRegistryMock()


@pytest.fixture
def api(registry) -> ExtensionApi:
    return ExtensionApi(
        presenter_registry=registry,
        type_registry=Dummy("TypeRegistry"),
        interpretation_service=Dummy("InterpretationService"),
        view_factory=Dummy("ViewFactory"),
        view_factory_registry=Dummy("ViewFactoryRegistry"),
        type_loader=Dummy("TypeLoader"),
    )


def test_create_column_based_presenter_extension(api, registry):
    create_extension(api)
    assert registry.register_presenter_count == 1


def test_destroy_column_based_presenter_extension(api, registry):
    destroy_extension(api)
    assert registry.deregister_presenter_count == 1


def test_everything_created_is_destroyed(api, registry):
    create_extension(api)
    destroy_extension(api)
    assert registry.register_presenter_count == registry.deregister_presenter_count
