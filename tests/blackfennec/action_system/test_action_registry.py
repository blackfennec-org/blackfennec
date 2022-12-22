import pytest

from blackfennec.action_system import ActionRegistry
from blackfennec_doubles.action_system import ActionMock
from blackfennec_doubles.type_system import TypeMock

def test_can_construct():
    registry = ActionRegistry()
    assert registry is not None

def test_can_register_action():
    registry = ActionRegistry()
    type = TypeMock()
    action = ActionMock(type)
    registry.register_action(action)
    assert action in registry.actions[type]

def test_can_register_two_actions_with_same_type():
    registry = ActionRegistry()
    type = TypeMock()
    action1 = ActionMock(type)
    action2 = ActionMock(type)
    registry.register_action(action1)
    registry.register_action(action2)
    assert action1 in registry.actions[type]
    assert action2 in registry.actions[type]

def test_can_deregister_action():
    registry = ActionRegistry()
    type = TypeMock()
    action = ActionMock(type)
    registry.register_action(action)
    registry.deregister_action(action)
    assert action not in registry.actions[type]

def test_cannot_deregister_action_twice():
    registry = ActionRegistry()
    type = TypeMock()
    action = ActionMock(type)
    registry.register_action(action)
    registry.deregister_action(action)
    with pytest.raises(AssertionError):
        registry.deregister_action(action)

def test_only_deregisters_correct_action():
    registry = ActionRegistry()
    type = TypeMock()
    action1 = ActionMock(type)
    action2 = ActionMock(type)
    registry.register_action(action1)
    registry.register_action(action2)
    registry.deregister_action(action1)
    assert action2 in registry.actions[type]

def test_returns_empty_list_by_default():
    registry = ActionRegistry()
    type = TypeMock()
    assert registry.get_actions(type) == []

def test_can_get_actions():
    registry = ActionRegistry()
    type = TypeMock()
    action1 = ActionMock(type)
    action2 = ActionMock(type)
    registry.register_action(action1)
    registry.register_action(action2)
    actions = registry.get_actions(type)
    assert len(actions) == 2
