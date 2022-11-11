from collections import deque

import pytest

from blackfennec_doubles.interpretation.double_interpretation import \
    InterpretationMock
from blackfennec_doubles.interpretation.double_interpretation_service import \
    InterpretationServiceMock
from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.structure.double_map import MapInstanceMock, MapMock
from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.type_system.double_type_registry import TypeRegistryMock
from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.type_system.double_type import TypeMock
from blackfennec.structure.root_factory import RootFactory
from core.map.map_view_model import MapViewModel


@pytest.fixture
def interpretation():
    structure = MapInstanceMock()
    RootFactory.make_root(structure)
    return InterpretationMock(structure)


@pytest.fixture
def interpretation_service(interpretation):
    return InterpretationServiceMock(deque([interpretation]))


@pytest.fixture
def type_registry():
    return TypeRegistryMock([
        TypeMock(Dummy('structure'))
    ])


@pytest.fixture
def view_model(interpretation, interpretation_service, type_registry):
    return MapViewModel(
        interpretation,
        interpretation_service,
        type_registry)


def test_can_construct(view_model):
    assert view_model


def test_can_get_value(view_model):
    assert view_model.value.value == {}


def test_can_add_item(view_model):
    key = 'Key'
    value = StructureMock()
    view_model.add_item(key, value)
    assert key in view_model.value.value


def test_can_delete_item(view_model):
    key = 'Key'
    value = StructureMock()
    view_model.add_item(key, value)
    view_model.delete_item(key)
    assert key not in view_model.value.value


def test_can_forward_navigation_request(view_model, interpretation):
    route_target = StructureMock()
    view_model.navigate_to(route_target)
    assert interpretation.navigation_requests == [route_target]


def test_can_create_preview(view_model, interpretation_service):
    preview = view_model.create_preview(StructureMock())
    last_spec = interpretation_service.last_specification
    assert last_spec.is_request_for_preview
    assert preview.navigation_service


def test_can_rename_key(view_model):
    view_model.add_item('old_key', StructureMock())
    view_model.rename_key('old_key', 'new_key')
    assert 'new_key' in view_model.value.value
    assert 'old_key' not in view_model.value.value


def test_can_rename_without_corrupting_structure(view_model):
    parent = MapInstanceMock({ 'child': view_model.value})
    view_model.add_item('old_key', StructureMock())
    view_model.rename_key('old_key', 'new_key')
    assert parent.value['child'] == view_model.value


def test_can_get_templates(view_model, type_registry):
    templates = view_model.get_templates()
    assert templates == type_registry.types


def test_can_add_by_template(view_model):
    key = 'key'
    structure = StructureMock(value='structure')
    template = TypeMock(default=structure)
    view_model.add_by_template(key, template)
    assert view_model.value.value[key] == structure
