import unittest
from typing import Optional

import pytest

from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.structure.double_string import StringMock
from blackfennec_doubles.layers.encapsulation_base.double_factory_base_visitor import \
    FactoryBaseVisitorMock
from blackfennec.layers.encapsulation_base.encapsulation_base import \
    EncapsulationBase
from blackfennec.layers.encapsulation_base.map_encapsulation_base import \
    MapEncapsulationBase
from blackfennec.layers.encapsulation_base.base_factory_visitor import \
    _create_generic_class
from blackfennec.structure.structure import Structure
from blackfennec.structure.map import Map
from tests.test_utils.observer import Observer


@pytest.fixture
def visitor():
    return FactoryBaseVisitorMock()


@pytest.fixture
def subject():
    return Map()


@pytest.fixture
def map_encapsulation_base(visitor, subject) -> MapEncapsulationBase:
    return MapEncapsulationBase(visitor, subject)


def test_can_construct(map_encapsulation_base):
    assert isinstance(map_encapsulation_base, MapEncapsulationBase)


def test_subject_getter(map_encapsulation_base, subject):
    assert map_encapsulation_base.subject == subject


def test_add_item_item(map_encapsulation_base):
    key = 'test'
    value = StringMock('test_value')
    map_encapsulation_base.add_item(key, value)
    assert value == map_encapsulation_base.subject.value[key]


def test_add_item_item_already_encapsulated(map_encapsulation_base, visitor):
    key = 'test'
    value = StringMock('test_value')
    type_class = _create_generic_class(EncapsulationBase)
    encapsulated = type_class(visitor, value)
    map_encapsulation_base.add_item(key, encapsulated)
    assert value == map_encapsulation_base.subject.value[key]


def test_get_value(visitor):
    key = 'test'
    subject_content = StringMock('test')
    subject = Map({key: subject_content})
    map_encapsulation_base = MapEncapsulationBase(
        visitor,
        subject
    )
    value = map_encapsulation_base.value
    assert subject_content == value[key]


def test_can_get_value_empty(map_encapsulation_base):
    assert isinstance(map_encapsulation_base.value, dict)


def test_set_value(map_encapsulation_base):
    key = 'test'
    value = StringMock('test')
    map_encapsulation_base.value = {key: value}
    assert value == map_encapsulation_base.subject.value[key]


def test_remove_item(map_encapsulation_base, visitor, subject):
    key = 'test'
    value = StringMock('test')
    subject.add_item(key, value)
    map_encapsulation_base.remove_item(key)
    assert len(subject.value) == 0


def test_remove_item_not_in_map(map_encapsulation_base):
    key = 'test'
    with pytest.raises(KeyError):
        map_encapsulation_base.remove_item(key)


def test_dispatch_change_notification(
        map_encapsulation_base,
        visitor,
        subject
):
    key = 'test'
    observer = Observer()
    map_encapsulation_base.bind(changed=observer.endpoint)

    map_encapsulation_base.add_item(key, StringMock('test'))

    assert observer.last_call[0][0] == subject
    assert visitor.visit_string_count == 1

    def test_can_get_repr(map_encapsulation_base):
        representation: str = map_encapsulation_base.__repr__()
        assert representation.startswith('MapEncapsulationBase(')
