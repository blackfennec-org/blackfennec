from blackfennec_doubles.actions.double_context import ContextMock
from core.string.actions.to_upper import ToUpperAction
from core import CORE_EXTENSION


def test_can_construct():
    action = ToUpperAction()
    assert action is not None


def test_can_execute():
    action = ToUpperAction()
    context = ContextMock()
    context.structure.value = "hello"
    action.execute(context)
    assert context.structure.value == "HELLO"


def test_is_correct_type():
    action = ToUpperAction()
    assert action.type is CORE_EXTENSION.types.string


def test_has_correct_name():
    action = ToUpperAction()
    assert action.name == "to upper"


def test_has_correct_description():
    action = ToUpperAction()
    assert len(action.description) > 7
