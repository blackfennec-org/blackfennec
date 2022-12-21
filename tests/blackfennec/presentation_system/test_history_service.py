import pytest
from enum import Enum
import random
import string

from blackfennec.presentation_system.history_service import HistoryService
from blackfennec_doubles.structure.double_structure import \
    NotifyingStructureMock


@pytest.fixture
def history():
    return HistoryService()


@pytest.fixture
def structure(history):
    structure = NotifyingStructureMock(value='original')
    history.observe(structure)
    return structure


def test_can_construct(history):
    assert history


def test_can_append(history, structure):
    structure.value = 'new'
    assert history.can_undo()


def test_can_tell_if_can_redo(history, structure):
    structure.value = 'new'
    history.undo()
    assert history.can_redo()


def test_can_redo(history):
    assert not history.can_redo()


def test_can_undo(history):
    assert not history.can_undo()


Action = Enum('Action', ['UNDO', 'REDO', 'CHANGE', 'RESULT'])


def random_string():
    return ''.join(random.choice(string.hexdigits) for _ in range(16))


@pytest.mark.parametrize('scenario', [
    ([Action.RESULT, Action.CHANGE, Action.UNDO]),
    ([Action.CHANGE, Action.RESULT, Action.UNDO, Action.REDO]),
    ([Action.RESULT, Action.CHANGE, Action.CHANGE, Action.UNDO, Action.UNDO]),
    ([Action.CHANGE, Action.CHANGE, Action.RESULT, Action.UNDO, Action.UNDO,
      Action.REDO, Action.REDO]),
    ([Action.CHANGE, Action.RESULT, Action.UNDO, Action.REDO, Action.UNDO,
      Action.REDO]),
    ([Action.CHANGE, Action.UNDO, Action.CHANGE, Action.RESULT, Action.UNDO,
      Action.REDO]),
])
def test_can_undo_redo(structure, history, scenario):
    for action in scenario:
        match action:
            case Action.UNDO:
                assert history.can_undo()
                history.undo()
            case Action.REDO:
                assert history.can_redo()
                history.redo()
            case Action.RESULT:
                result = structure.value
            case Action.CHANGE:
                structure.value = random_string()

    assert structure.value == result
