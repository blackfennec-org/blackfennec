# -*- coding: utf-8 -*-

import pytest

from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec.structure.reference_navigation.root_navigator import RootNavigator


@pytest.fixture()
def root():
    return StructureMock()


@pytest.fixture()
def root_child(root):
    return StructureMock(root=root)


@pytest.fixture()
def root_navigator():
    return RootNavigator()


def test_can_construct(root_navigator):
    assert isinstance(root_navigator, RootNavigator)


def test_get_representation(root_navigator):
    assert str(root_navigator)


def test_navigate(root_navigator, root, root_child):
    assert root_navigator.navigate(root_child) == root
