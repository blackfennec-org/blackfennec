# -*- coding: utf-8 -*-
import logging

import pytest

from doubles.black_fennec.structure.double_list import ListInstanceMock
from doubles.black_fennec.structure.double_map import MapInstanceMock
from doubles.black_fennec.structure.double_structure import StructureMock
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.reference_navigation.index_of_navigator import IndexOfNavigator
from src.black_fennec.structure.string import String
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.reference_navigation.navigator import Navigator


@pytest.fixture()
def list():
    return ListInstanceMock(value=[
        StructureMock(),
        StructureMock(),
        StructureMock(),
        StructureMock(),
        StructureMock(),
    ])


@pytest.fixture()
def map():
    return MapInstanceMock(value={
        'key': StructureMock(),
        'key2': StructureMock(),
        '0': StructureMock(),
        '1': StructureMock(),
    })


@pytest.fixture()
def index_of_navigator():
    return IndexOfNavigator()


def test_can_construct(index_of_navigator):
    assert isinstance(index_of_navigator, IndexOfNavigator)


def test_get_representation(index_of_navigator):
    assert str(index_of_navigator)


@pytest.mark.parametrize("child_index", [
    0,
    1,
    2,
    3,
    4,
])
def test_navigate_list(list, child_index):
    navigator = IndexOfNavigator()
    assert navigator.navigate(list.value[child_index]).value == child_index


def test_navigate_from_child_without_parent(list):
    navigator = IndexOfNavigator()
    with pytest.raises(TypeError):
        navigator.navigate(StructureMock())


@pytest.mark.parametrize("child_key", [
    'key',
    'key2',
    '1',
    '0',
])
def test_navigate_map(map, child_key):
    navigator = IndexOfNavigator()
    assert navigator.navigate(map.value[child_key]).value == child_key
