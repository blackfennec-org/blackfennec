# -*- coding: utf-8 -*-
import pytest

from blackfennec_doubles.double_dummy import Dummy
from blackfennec.extension.extension_api import ExtensionApi


@pytest.fixture
def presenter_registry():
    return Dummy('PresenterRegistry')


@pytest.fixture
def type_registry():
    return Dummy('TypeRegistry')


@pytest.fixture
def interpretation_service():
    return Dummy('InterpretationService')


@pytest.fixture
def view_factory():
    return Dummy('ViewFactory')


@pytest.fixture
def view_factory_registry():
    return Dummy('ViewFactoryRegistry')


@pytest.fixture
def type_loader():
    return Dummy('TypeLoader')


@pytest.fixture
def action_registry():
    return Dummy('ActionRegistry')


@pytest.fixture
def document_registry():
    return Dummy('DocumentRegistry')


@pytest.fixture
def document_factory():
    return Dummy('DocumentFactory')


@pytest.fixture
def ui_service_registry():
    return Dummy('UiServiceRegistry')


@pytest.fixture
def extension_api(
        presenter_registry, type_registry, interpretation_service,
        view_factory, view_factory_registry, type_loader, action_registry,
        document_registry, document_factory, ui_service_registry
):
    return ExtensionApi(
        presenter_registry,
        type_registry,
        interpretation_service,
        view_factory,
        view_factory_registry,
        type_loader,
        action_registry,
        document_registry,
        document_factory,
        ui_service_registry,
    )


def test_can_construct(extension_api):
    assert isinstance(extension_api, ExtensionApi)


def test_can_get_presenter_registry(extension_api, presenter_registry):
    assert extension_api.presenter_registry == presenter_registry


def test_can_get_type_registry(extension_api, type_registry):
    assert extension_api.type_registry == type_registry


def test_can_get_interpretation_service(extension_api, interpretation_service):
    assert extension_api.interpretation_service == interpretation_service


def test_can_get_view_factory(extension_api, view_factory):
    assert extension_api.view_factory == view_factory


def test_can_get_view_factory_registry(extension_api, view_factory_registry):
    assert extension_api.view_factory_registry == view_factory_registry


def test_can_get_type_loader(extension_api, type_loader):
    assert extension_api.type_loader == type_loader


def test_can_get_action_registry(extension_api, action_registry):
    assert extension_api.action_registry == action_registry


def test_can_get_document_registry(extension_api, document_registry):
    assert extension_api.document_registry == document_registry


def test_can_get_document_factory(extension_api, document_factory):
    assert extension_api.document_factory == document_factory


def test_can_get_ui_service_registry(extension_api, ui_service_registry):
    assert extension_api.ui_service_registry == ui_service_registry
