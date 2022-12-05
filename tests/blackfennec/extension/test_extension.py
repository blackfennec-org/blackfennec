# -*- coding: utf-8 -*-
import pytest

from blackfennec.extension.extension import Extension
from blackfennec_doubles.double_dummy import Dummy


@pytest.fixture
def extension():
    return Extension(
        name='test',
        api=Dummy('ExtensionApi'),
        dependencies={'core'},
    )


def test_can_construct_extension(extension):
    assert extension


def test_can_get_name(extension):
    assert extension.name == 'test'


def test_can_get_dependencies(extension):
    assert extension.dependencies == {'core'}


def test_can_get_is_active(extension):
    assert not extension.is_active


def test_can_activate(extension):
    extension.activate()
    assert extension.is_active


def test_can_deactivate(extension):
    extension.activate()
    extension.deactivate()
    assert not extension.is_active
