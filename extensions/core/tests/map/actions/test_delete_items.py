import pytest

from blackfennec_doubles.actions.double_context import ContextMock
from core.map.actions.delete_items import DeleteMapItemsAction
from core import CORE_EXTENSION


@pytest.fixture
def action():
    return DeleteMapItemsAction()


def test_can_construct(action):
    assert action is not None


def test_can_execute(action):
    context = ContextMock()
    context.structure.value = {"test"}
    action.execute(context)
    assert context.structure.value == {}


def test_is_correct_type(action):
    assert action.type is CORE_EXTENSION.types.map


def test_has_correct_name(action):
    assert action.name == "delete items"


def test_has_correct_description(action):
    assert len(action.description) > 7
