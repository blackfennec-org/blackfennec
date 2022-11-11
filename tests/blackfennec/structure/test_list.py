import pytest
from tests.test_utils.observer import Observer
from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.structure.double_root import RootMock
from blackfennec_doubles.layers.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from blackfennec.structure.list import List

from tests.test_utils.parameterize import CORE_TYPE_FACTORIES

def test_can_construct():
    test_list = List()
    assert test_list.value == []

def test_can_construct_from_list():
    test_list = List([StructureMock()])
    assert len(test_list.value) == 1

def test_can_add_item_item():
    test_list = List()
    value = StructureMock()
    test_list.add_item(value)
    assert value in test_list.value

def test_add_item_does_set_parent():
    test_list = List()
    value = StructureMock()
    test_list.add_item(value)
    assert value.parent is test_list

def test_add_item_throws_on_parent_not_none():
    test_list = List()
    value = RootMock()

    with pytest.raises(AssertionError):
        test_list.add_item(value)

def test_add_item_logs_on_parent_not_none():
    test_list = List()
    value = RootMock()

    with pytest.raises(AssertionError):
        test_list.add_item(value)

def test_can_remove_item_item():
    test_list = List()
    value = StructureMock()
    test_list.add_item(value)
    test_list.remove_item(value)
    assert value not in test_list.value

def test_remove_item_does_unset_parent():
    test_list = List()
    value = StructureMock()
    test_list.add_item(value)
    test_list.remove_item(value)
    assert value.parent is None

def test_remove_item_throws_on_delete_of_not_existing_item():
    test_list = List()
    not_value = StructureMock()

    with pytest.raises(ValueError):
        test_list.remove_item(not_value)

def test_can_get_value():
    value = StructureMock('value')
    structure_list = List([value])
    assert value in structure_list.value

def test_can_set_value():
    value = StructureMock('value')
    structure_list = List()
    structure_list.value = [value]
    assert value in structure_list.value


def test_notifies_on_value_change():
    observer = Observer()
    structure = List()
    structure.bind(value=observer.endpoint)
    new_value = [StructureMock()]
    structure.value = new_value

    assert observer.last_call == ((structure, new_value), {})


def test_accept():
    visitor = FactoryBaseVisitorMock()
    structure_list = List()
    structure_list.accept(visitor)
    assert visitor.visit_list_count == 1

@pytest.mark.parametrize(**CORE_TYPE_FACTORIES)
def test_can_add_all_core_types(create_structure):
    a = create_structure()
    b = create_structure()

    m = List()
    m.add_item(a)
    m.add_item(b)

    m.remove_item(a)

    assert m.value[0] is b
