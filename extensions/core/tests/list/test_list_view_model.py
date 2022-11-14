import pytest
from collections import deque

from blackfennec_doubles.actions import ActionRegistryMock
from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.interpretation.double_interpretation_service import InterpretationServiceMock
from blackfennec_doubles.structure.double_list import ListInstanceMock
from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.type_system.double_type_registry import TypeRegistryMock
from blackfennec_doubles.type_system.double_type import TypeMock
from core.list.list_view_model import ListViewModel


@pytest.fixture
def bf_type():
    return TypeMock(Dummy('structure'))


@pytest.fixture
def interpretation(bf_type):
    structure = ListInstanceMock()
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
    return ListViewModel(
        interpretation,
        interpretation_service,
        type_registry,
        action_registry,
    )


def test_can_construct(view_model):
    assert isinstance(view_model, ListViewModel)


def test_can_get_value(view_model):
    assert view_model.list.value == []


def test_can_forward_navigation_request(view_model, interpretation):
    route_target = StructureMock()
    view_model.navigate_to(route_target)
    assert interpretation.navigation_requests == [route_target]


def test_can_create_preview(view_model, interpretation_service, interpretation):
    interpretation = view_model.create_interpretation(StructureMock())
    assert interpretation_service.last_specification.is_request_for_preview
    assert interpretation.navigation_service is not None


def test_can_add_by_template(view_model):
    subject = StructureMock()
    template = TypeMock(default=subject)
    view_model.add_by_template(template)
    assert subject in view_model.list.value


def test_can_get_templates(view_model, type_registry):
    subject = StructureMock()
    template = TypeMock(subject)
    type_registry.types.append(template)
    templates = view_model.get_templates()
    assert template in templates


def test_can_get_actions(view_model, action_registry):
    actions = view_model.get_actions(Dummy('structure'))
    assert str(actions.pop()) == "action"
