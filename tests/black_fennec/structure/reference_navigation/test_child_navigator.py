# -*- coding: utf-8 -*-
import logging
from typing import Union

import pytest

from doubles.black_fennec.structure.double_structure import StructureMock
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.reference_navigation.child_navigator import ChildNavigator
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.reference_navigation.navigator import Navigator


@pytest.fixture()
def list():
    return List([
        StructureMock(),
        StructureMock(),
        StructureMock(),
        StructureMock(),
        StructureMock(),
    ])


@pytest.fixture()
def map():
    return Map({
        'key': StructureMock(),
        'key2': StructureMock(),
        '0': StructureMock(),
        '1': StructureMock(),
    })


def test_can_construct():
    navigator = ChildNavigator('child')
    assert isinstance(navigator, ChildNavigator)


def test_get_representation():
    navigator = ChildNavigator('child')
    assert str(navigator) == 'child'


@pytest.mark.parametrize("child_index", [
    0,
    1,
    2,
    3,
    4,
])
def test_navigate_list(list, child_index):
    navigator = ChildNavigator(child_index)
    assert navigator.navigate(list) == list.value[child_index]


@pytest.mark.parametrize("child_key", [
    'key',
    'key2',
    '0',
    '1',
])
def test_navigate_map(map, child_key):
    navigator = ChildNavigator(child_key)
    assert navigator.navigate(map) == map.value[child_key]


def test_navigate_list_invalid_index(list):
    navigator = ChildNavigator('5')
    with pytest.raises(IndexError):
        navigator.navigate(list)


def test_navigate_map_invalid_key(map):
    navigator = ChildNavigator('invalid_key')
    with pytest.raises(KeyError):
        navigator.navigate(map)


def test_navigate_invalid_type():
    navigator = ChildNavigator('token')
    with pytest.raises(TypeError):
        navigator.navigate(StructureMock())


def test_navigators_are_equal():
    assert ChildNavigator('token') == ChildNavigator('token')


def test_navigators_are_not_equal():
    assert ChildNavigator('token') != ChildNavigator('token2')


def test_hash_equal_tokens():
    assert hash(ChildNavigator('token')) == hash(ChildNavigator('token'))


def test_hash_not_equal_tokens():
    assert hash(ChildNavigator('token')) != hash(ChildNavigator('token2'))
