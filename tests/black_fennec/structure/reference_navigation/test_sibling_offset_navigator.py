# -*- coding: utf-8 -*-
import pytest

from doubles.black_fennec.structure.double_list import ListInstanceMock
from doubles.black_fennec.structure.double_structure import StructureMock
from src.black_fennec.structure.reference_navigation.sibling_offset_navigator import SiblingOffsetNavigator


@pytest.fixture()
def structure():
    return ListInstanceMock(value=[
        StructureMock(),
        StructureMock(),
        StructureMock(),
        StructureMock(),
        StructureMock()
    ])


def test_can_construct():
    navigator = SiblingOffsetNavigator(0)
    assert isinstance(navigator, SiblingOffsetNavigator)


def test_get_representation():
    navigator = SiblingOffsetNavigator(0)
    assert str(navigator) == 'sibling(0)'


@pytest.mark.parametrize("offset, child_index", [
    (0, 1),
    (1, 1),
    (-1, 1),
    (4, 0),
    (-4, 4),
])
def test_navigate(structure, offset, child_index):
    navigator = SiblingOffsetNavigator(offset)
    assert navigator.navigate(structure.value[child_index]) == structure.value[child_index + offset]


def test_navigators_with_same_offset_are_equal():
    navigator = SiblingOffsetNavigator(0)
    assert navigator == SiblingOffsetNavigator(0)


def test_navigators_with_different_offset_are_not_equal():
    navigator = SiblingOffsetNavigator(0)
    assert navigator != SiblingOffsetNavigator(1)


def test_hash_of_navigators_with_same_offset_are_equal():
    navigator = SiblingOffsetNavigator(0)
    assert hash(navigator) == hash(SiblingOffsetNavigator(0))


def test_hash_of_navigators_with_different_offset_are_not_equal():
    navigator = SiblingOffsetNavigator(0)
    assert hash(navigator) != hash(SiblingOffsetNavigator(1))
