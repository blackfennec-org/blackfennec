import pytest

from blackfennec_doubles.actions.double_context import ContextMock
from core.number.actions.to_integer import ToIntegerAction
from core import CORE_EXTENSION


@pytest.fixture
def action():
    return ToIntegerAction()


def test_can_construct(action):
    assert action is not None


def test_can_execute(action):
    context = ContextMock()
    context.structure.value = 1.0001
    action.execute(context)
    assert context.structure.value == 1


def test_is_correct_type(action):
    assert action.type is CORE_EXTENSION.types.number


def test_has_correct_name(action):
    assert action.name == "to integer"


def test_has_correct_description(action):
    assert len(action.description) > 7
