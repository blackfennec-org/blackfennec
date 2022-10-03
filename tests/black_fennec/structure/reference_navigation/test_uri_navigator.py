# -*- coding: utf-8 -*-
import logging

import pytest

from doubles.black_fennec.structure.double_root import RootMock
from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.util.document.double_document import DocumentMock
from doubles.black_fennec.util.document.double_document_factory import DocumentFactoryMock
from doubles.double_dummy import Dummy
from src.black_fennec.structure.reference_navigation.uri_navigator import UriNavigator
from src.black_fennec.structure.structure import Structure
from src.black_fennec.util.document.document import Document
from src.black_fennec.util.document.document_factory import DocumentFactory
from src.black_fennec.structure.reference_navigation.navigator import Navigator


@pytest.fixture()
def document():
    return DocumentMock(
        location='http://example.com',
        content=StructureMock(value='content')
    )


@pytest.fixture()
def root(document):
    return RootMock(document=document)


@pytest.fixture()
def structure(root):
    return StructureMock(parent=root, root=root)


@pytest.fixture()
def document_factory(document):
    return DocumentFactoryMock(create_return=document)


@pytest.fixture()
def uri_navigator(document_factory):
    return UriNavigator(document_factory, 'http://example.com/test')


def test_can_construct(uri_navigator):
    assert isinstance(uri_navigator, UriNavigator)


def test_get_representation(uri_navigator):
    assert str(uri_navigator) == 'http://example.com/test'


def test_navigate(uri_navigator, structure, document_factory, document):
    result = uri_navigator.navigate(structure)
    assert document_factory.create_count == 1
    assert document.load_content_count == 1
    assert result.value == 'content'


def test_navigators_with_same_offset_are_equal():
    navigator = UriNavigator(Dummy(), 'test')
    assert navigator == UriNavigator(Dummy(), 'test')


def test_navigators_with_different_offset_are_not_equal():
    navigator = UriNavigator(Dummy(), 'test1')
    assert navigator != UriNavigator(Dummy(), 'test2')


def test_hash_of_navigators_with_same_offset_are_equal():
    navigator = UriNavigator(Dummy(), 'test')
    assert hash(navigator) == hash(UriNavigator(Dummy(), 'test'))


def test_hash_of_navigators_with_different_offset_are_not_equal():
    navigator = UriNavigator(Dummy(), 'test1')
    assert hash(navigator) != hash(UriNavigator(Dummy(), 'test2'))
