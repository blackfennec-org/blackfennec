import random
import string
from enum import Enum

import pytest

from blackfennec.layers.overlay.overlay_factory_visitor import \
    OverlayFactoryVisitor
from blackfennec.structure.map import Map
from blackfennec.structure.list import List
from blackfennec.structure.string import String
from blackfennec.structure.number import Number
from blackfennec.structure.boolean import Boolean

from blackfennec.layers.history.history import History
from blackfennec.layers.history.history_factory_visitor import \
    HistoryFactoryVisitor

pytestmark = pytest.mark.integration


@pytest.fixture
def structure():
    return Map({
        "map": Map({
            "boolean": Boolean()
        }),
        "list": List([Number(1337)]),
        "string": String("Leet")
    })


@pytest.fixture
def history():
    return History()


@pytest.fixture
def visitor(history):
    return HistoryFactoryVisitor(history)


@pytest.fixture
def historized(structure, visitor):
    return structure.accept(visitor)


def test_can_create_layer(historized):
    assert historized


def test_can_undo_modification_on_string(history, historized):
    historized.value["string"].value = "Speak"
    history.undo()
    assert historized.value["string"].value == "Leet"


def test_can_undo_modification_on_number_in_list(history, historized):
    historized.value["list"].value[0].value = 3.141
    history.undo()
    assert historized.value["list"].value[0].value == 1337


def test_can_undo_add_on_list(history, historized):
    historized.value["list"].add_item(Number(3.141))
    history.undo()
    assert len(historized.value["list"].value) == 1


Action = Enum(
    'Action',
    ['UNDO', 'REDO', 'CHANGE', 'ADD_ITEM', 'REMOVE_ITEM', 'RESULT']
)


def random_string():
    return ''.join(random.choice(string.hexdigits) for _ in range(16))


SCENARIOS = [
    ([Action.RESULT, Action.CHANGE, Action.UNDO]),
    ([Action.CHANGE, Action.RESULT, Action.UNDO, Action.REDO]),
    ([Action.RESULT, Action.CHANGE, Action.CHANGE, Action.UNDO, Action.UNDO]),
    ([Action.CHANGE, Action.CHANGE, Action.RESULT, Action.UNDO, Action.UNDO,
      Action.REDO, Action.REDO]),
    ([Action.CHANGE, Action.RESULT, Action.UNDO, Action.REDO, Action.UNDO,
      Action.REDO]),
    ([Action.CHANGE, Action.UNDO, Action.CHANGE, Action.RESULT, Action.UNDO,
      Action.REDO]),
    ([Action.RESULT, Action.ADD_ITEM, Action.UNDO]),
    ([Action.RESULT, Action.ADD_ITEM, Action.ADD_ITEM, Action.UNDO,
      Action.UNDO]),
    ([Action.RESULT, Action.ADD_ITEM, Action.ADD_ITEM, Action.UNDO,
      Action.REMOVE_ITEM]),
    ([Action.RESULT, Action.ADD_ITEM, Action.REMOVE_ITEM, Action.UNDO,
      Action.UNDO]),
]


@pytest.mark.parametrize('scenario', SCENARIOS)
def test_can_undo_redo_on_list(history, historized, scenario):
    list_structure = historized.value["list"]
    for action in scenario:
        match action:
            case Action.UNDO:
                assert history.can_undo()
                history.undo()
            case Action.REDO:
                assert history.can_redo()
                history.redo()
            case Action.RESULT:
                result = list_structure.structure.value
            case Action.CHANGE:
                list_structure.value = [String(random_string())]
            case Action.ADD_ITEM:
                list_structure.add_item(String(random_string()))
            case Action.REMOVE_ITEM:
                list_structure.remove_item(
                    random.choice(
                        [
                            value for value in list_structure.value
                            if isinstance(value.structure, String)
                        ]
                    )
                )
    assert historized.value["list"].structure.value == result


@pytest.mark.parametrize('scenario', SCENARIOS)
def test_can_undo_redo_on_map(history, historized, scenario):
    map_structure = historized.value["map"]
    for action in scenario:
        match action:
            case Action.UNDO:
                assert history.can_undo()
                history.undo()
            case Action.REDO:
                assert history.can_redo()
                history.redo()
            case Action.RESULT:
                result = map_structure.structure.value
            case Action.CHANGE:
                map_structure.value = {
                    random_string(): String(random_string())}
            case Action.ADD_ITEM:
                map_structure.add_item(random_string(),
                                       String(random_string()))
            case Action.REMOVE_ITEM:
                map_structure.remove_item(
                    random.choice(
                        [key for key in map_structure.value.keys() if
                         key != "boolean"]
                    )
                )

    assert historized.value["map"].structure.value == result


def test_can_undo_redo_on_top_level_map(history, historized):
    result1 = historized.structure.value
    historized.add_item("number", Number(1337))
    result2 = historized.structure.value
    historized.remove_item("number")
    history.undo()
    assert historized.structure.value == result2
    history.undo()
    assert historized.structure.value == result1


def test_can_undo_redo_on_overlayed_top_level_map(history, historized):
    overlay = historized.accept(OverlayFactoryVisitor())
    test_can_undo_redo_on_top_level_map(history, overlay)


@pytest.mark.parametrize('scenario', SCENARIOS)
def test_can_undo_redo_on_overlayed_map(history, historized, scenario):
    overlay = historized.accept(OverlayFactoryVisitor())
    test_can_undo_redo_on_map(history, overlay, scenario)


@pytest.mark.xfail
@pytest.mark.parametrize('scenario', SCENARIOS)
def test_can_undo_redo_on_overlayed_list(history, historized, scenario):
    overlay = historized.accept(OverlayFactoryVisitor())
    test_can_undo_redo_on_list(history, overlay, scenario)
