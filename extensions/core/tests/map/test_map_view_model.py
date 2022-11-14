from collections import deque

import pytest

from blackfennec_doubles.actions import ActionRegistryMock
from blackfennec_doubles.interpretation.double_interpretation import \
    InterpretationMock
from blackfennec_doubles.interpretation.double_interpretation_service import \
    InterpretationServiceMock
from blackfennec_doubles.structure.double_map import MapInstanceMock
from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.type_system.double_type_registry import TypeRegistryMock
from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.type_system.double_type import TypeMock
from core.map.map_view_model import MapViewModel


@pytest.fixture
def bf_type():
    return TypeMock(Dummy('structure'))


@pytest.fixture
def interpretation(bf_type):
    structure = MapInstanceMock()
    return InterpretationMock(structure, types=[bf_type])


@pytest.fixture
def interpretation_service(interpretation):
    return InterpretationServiceMock(deque([interpretation]))


@pytest.fixture
def type_registry(bf_type):
    return TypeRegistryMock([
        bf_type
    ])


@pytest.fixture
def action_registry(bf_type):
    return ActionRegistryMock({
        bf_type: [Dummy('action')]
    })


@pytest.fixture
def view_model(interpretation, interpretation_service, type_registry, action_registry):
    return MapViewModel(
        interpretation,
        interpretation_service,
        type_registry,
        action_registry,
    )


def test_can_construct(view_model):
    assert view_model


def test_can_get_value(view_model):
    assert view_model.map.value == {}


def test_can_forward_navigation_request(view_model, interpretation):
    route_target = StructureMock()
    view_model.navigate_to(route_target)
    assert interpretation.navigation_requests == [route_target]


def test_can_create_interpretation(view_model, interpretation_service):
    preview = view_model.create_interpretation(StructureMock())
    last_spec = interpretation_service.last_specification
    assert last_spec.is_request_for_preview
    assert preview.navigation_service


def test_can_rename_key(view_model):
    view_model.map.add_item('old_key', StructureMock())
    view_model.rename_key('old_key', 'new_key')
    assert 'new_key' in view_model.map.value
    assert 'old_key' not in view_model.map.value


def test_can_rename_without_corrupting_structure(view_model):
    parent = MapInstanceMock({'child': view_model.map})
    view_model.map.add_item('old_key', StructureMock())
    view_model.rename_key('old_key', 'new_key')
    assert parent.value['child'] == view_model.map


def test_can_get_templates(view_model, type_registry):
    templates = view_model.get_templates()
    assert templates == type_registry.types


def test_can_add_by_template(view_model):
    key = 'key'
    structure = StructureMock(value='structure')
    template = TypeMock(default=structure)
    view_model.add_by_template(key, template)
    assert view_model.map.value[key] == structure


def test_can_get_actions(view_model, action_registry):
    actions = view_model.get_actions(Dummy('structure'))
    assert str(actions.pop()) == "action"
