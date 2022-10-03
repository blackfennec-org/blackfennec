# -*- coding: utf-8 -*-
import pytest

from doubles.black_fennec.structure.double_structure import StructureMock
from src.black_fennec.structure.reference_navigation.parent_navigator import ParentNavigator


@pytest.fixture()
def parent():
    return StructureMock()


@pytest.fixture()
def child(parent):
    return StructureMock(parent=parent)


@pytest.fixture()
def parent_navigator():
    return ParentNavigator()


def test_can_construct(parent_navigator):
    assert isinstance(parent_navigator, ParentNavigator)


def test_get_representation(parent_navigator):
    assert str(parent_navigator)


def test_navigate(parent_navigator, parent, child):
    assert parent_navigator.navigate(child) == parent
