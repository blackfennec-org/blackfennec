import pytest

from blackfennec.facade.ui_service.ui_service_registry import UiServiceRegistry
from blackfennec_doubles.double_dummy import Dummy


@pytest.fixture
def ui_service_key():
    return Dummy('window')


@pytest.fixture
def ui_service():
    return Dummy('UiService')


@pytest.fixture
def ui_service_registry(ui_service, ui_service_key):
    return UiServiceRegistry()


def test_can_construct(ui_service_registry):
    assert isinstance(ui_service_registry, UiServiceRegistry)


def test_can_get_services(ui_service_registry):
    assert ui_service_registry.services == {}


def test_can_register_service(ui_service_registry, ui_service, ui_service_key):
    ui_service_registry.register(ui_service_key, ui_service)
    assert ui_service_registry.services[ui_service_key] == ui_service


def test_can_unregister_service(ui_service_registry, ui_service, ui_service_key):
    ui_service_registry.register(ui_service_key, ui_service)
    assert ui_service_registry.services[ui_service_key] == ui_service
    ui_service_registry.unregister(ui_service_key)
    assert ui_service_registry.services == {}
