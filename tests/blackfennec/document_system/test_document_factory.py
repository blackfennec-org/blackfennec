# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pytest

from blackfennec_doubles.document_system.double_document import DocumentMock
from blackfennec_doubles.document_system.mime_type.double_mime_type_registry import MimeTypeRegistryMock
from blackfennec_doubles.document_system.resource_type.double_resource_type_registry import ResourceTypeRegistryMock
from blackfennec.document_system.document_factory import DocumentFactory


@pytest.fixture
def resource_type_registry():
    return ResourceTypeRegistryMock({'resource_type': None, 'https': None})


@pytest.fixture
def mime_type_registry():
    return MimeTypeRegistryMock({'mime_type': None, 'application/json': None})


@pytest.fixture
def document_factory(resource_type_registry, mime_type_registry):
    return DocumentFactory(
        resource_type_registry, 
        mime_type_registry, 
        DocumentMock)


def test_can_construct(document_factory):
    pass


def test_create_document(document_factory, mime_type_registry, resource_type_registry):
    document_factory.create("uri", "resource_type", "mime_type")
    assert mime_type_registry.mime_types_getter_count == 1
    assert resource_type_registry.resource_types_getter_count == 1


def test_create_document_without_mime_type(
        document_factory,
        mime_type_registry,
        resource_type_registry
):
    document_factory.create("https://test.com/test.json")
    assert mime_type_registry.mime_types_getter_count == 1
    assert resource_type_registry.resource_types_getter_count == 1


def test_get_document_for_created_document(document_factory):
    document = document_factory.create("uri", "resource_type", "mime_type")
    assert document_factory.get_document(document.content) == document
