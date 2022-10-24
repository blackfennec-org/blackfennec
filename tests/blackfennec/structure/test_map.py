import pytest
import logging

from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.structure.double_root import RootMock
from blackfennec_doubles.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from tests.test_utils.parameterize import CORE_TYPE_FACTORIES
from blackfennec.structure.map import Map


def test_can_construct():
    m = Map()

def test_can_construct_from_dict():
    data = {'a': StructureMock(), 'b': StructureMock()}
    structure = Map(data)
    assert structure.value == data

def test_can_add_item():
    m = Map()
    key = 'Key'
    value = StructureMock()
    m.add_item(key, value)
    assert key in m.value

def test_add_item_does_set_parent():
    m = Map()
    key = 'Key'
    value = StructureMock()
    m.add_item(key, value)
    assert value.parent is m

def test_add_item_throws_on_key_occupied():
    key = 'Key'
    value = StructureMock()
    m = Map({key: value})
    with pytest.raises(ValueError):
        m.add_item(key, value)

def test_add_item_logs_on_key_occupied(caplog):
    key = 'Key'
    value = StructureMock()
    m = Map({key: value})
    with pytest.raises(Exception):
        m.add_item(key, value)

    assert caplog.record_tuples[0][1] == logging.ERROR
    

def test_add_item_throws_on_parent_not_none():
    m = Map()
    key = 'Key'
    value = RootMock()

    with pytest.raises(AssertionError):
        m.add_item(key, value)

def test_add_item_raises_assertion_error():
    m = Map()
    key = 'Key'
    value = RootMock()

    with pytest.raises(AssertionError):
        m.add_item(key, value)

def test_can_remove_item():
    key = 'key'
    m = Map({
        key: StructureMock()
    })
    m.remove_item(key)
    assert key not in m.value

def test_remove_item_does_unset_parent():
    key = 'key'
    value = StructureMock()
    m = Map({
        key: value
    })
    m.remove_item(key)
    assert value.parent is None

def test_throws_on_remove_item_not_existing():
    m = Map()
    not_key = 'Not in Map'

    with pytest.raises(KeyError):
        m.remove_item(not_key)

def test_logs_on_remove_item_not_existing(caplog):
    m = Map()
    not_key = 'Not in Map'
    
    with pytest.raises(Exception):
        m.remove_item(not_key)
    
    assert caplog.record_tuples[0][1] == logging.ERROR

def test_can_get_value():
    key = 'key'
    value = StructureMock('value')
    structure_map = Map({key: value})
    assert structure_map.value[key] is value

def test_can_set_value():
    key = 'key'
    value = StructureMock('value')
    structure_map = Map()
    structure_map.value = {key: value}
    assert structure_map.value[key] is value

def test_can_set_value_when_map_has_content():
    key = 'key'
    value = StructureMock('value')
    structure_map = Map({key: value})
    structure_map.value = {key: value}
    assert structure_map.value[key] is value

def test_accept():
    visitor = FactoryBaseVisitorMock()
    structure_map = Map()
    structure_map.accept(visitor)
    assert visitor.visit_map_count == 1

@pytest.mark.parametrize(**CORE_TYPE_FACTORIES)
def test_can_add_all_core_types(create_structure):
    a = create_structure()
    b = create_structure()

    m = Map()
    m.add_item("A", a)
    m.add_item("B", b)

    m.remove_item("A")

    assert m.value["B"] is b
