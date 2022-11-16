import pytest

from blackfennec_doubles.actions.double_context import ContextMock
from core.boolean.actions.toggle_boolean import ToggleBooleanAction
from core.number.actions.to_integer import ToIntegerAction
from core import CORE_EXTENSION


@pytest.fixture
def action():
    return ToggleBooleanAction()


def test_can_construct(action):
    assert action is not None


def test_can_execute(action):
    context = ContextMock()
    context.structure.value = True
    action.execute(context)
    assert context.structure.value is False


def test_is_correct_type(action):
    assert action.type is CORE_EXTENSION.types.boolean


def test_has_correct_name(action):
    assert action.name == "toggle"


def test_has_correct_description(action):
    assert len(action.description) > 7
