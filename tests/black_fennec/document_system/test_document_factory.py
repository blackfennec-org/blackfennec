# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pytest

from doubles.black_fennec.document_system.double_document import DocumentMock
from doubles.black_fennec.document_system.mime_type.double_mime_type_registry import MimeTypeRegistryMock
from doubles.black_fennec.document_system.resource_type.double_resource_type_registry import ResourceTypeRegistryMock
from src.black_fennec.document_system.document_factory import DocumentFactory


class TestDocument:
    @pytest.fixture
    def resource_type_registry(self):
        return ResourceTypeRegistryMock({'resource_type': None})

    @pytest.fixture
    def mime_type_registry(self):
        return MimeTypeRegistryMock({'mime_type': None})

    @pytest.fixture
    def document_factory(self, resource_type_registry, mime_type_registry):
        return DocumentFactory(resource_type_registry, mime_type_registry, DocumentMock)

    def test_can_construct(self, document_factory):
        pass

    def test_create_document(self, document_factory, mime_type_registry, resource_type_registry):
        document_factory.create("uri", "resource_type", "mime_type")
        assert mime_type_registry.mime_types_getter_count == 1
        assert resource_type_registry.resource_types_getter_count == 1
