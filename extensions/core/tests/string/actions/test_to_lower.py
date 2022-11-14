from blackfennec_doubles.actions.double_context import ContextMock
from core.string.actions.to_lower import ToLowerAction
from core import CORE_EXTENSION


def test_can_construct():
    action = ToLowerAction()
    assert action is not None


def test_can_execute():
    action = ToLowerAction()
    context = ContextMock()
    context.structure.value = "HELLO"
    action.execute(context)
    assert context.structure.value == "hello"


def test_is_correct_type():
    action = ToLowerAction()
    assert action.type is CORE_EXTENSION.types.string


def test_has_correct_name():
    action = ToLowerAction()
    assert action.name == "to lower"


def test_has_correct_description():
    action = ToLowerAction()
    assert len(action.description) > 7
