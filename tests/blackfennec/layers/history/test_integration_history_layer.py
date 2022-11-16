import pytest

from blackfennec.structure.map import Map
from blackfennec.structure.list import List
from blackfennec.structure.string import String
from blackfennec.structure.number import Number
from blackfennec.structure.boolean import Boolean

from blackfennec.layers.history.history import History
from blackfennec.layers.history.history_factory_visitor import HistoryFactoryVisitor

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
def historied(structure, visitor):
    return structure.accept(visitor)

def test_can_create_layer(historied):
    assert historied

def test_can_undo_modification_on_string(history, historied):
    historied.value["string"].value = "Speak"
    history.undo()
    assert historied.value["string"].value == "Leet"

def test_can_undo_modification_on_number_in_list(history, historied):
    historied.value["list"].value[0].value = 3.141
    history.undo()
    assert historied.value["list"].value[0].value == 1337

def test_can_undo_modification_on_list(history, historied):
    historied.value["list"].add_item(Number(3.141))
    history.undo()
    assert len(historied.value["list"].value) == 1

def test_can_undo_modification_on_map(history, historied):
    historied.remove_item("map")
    history.undo()
    assert historied.value["map"]
