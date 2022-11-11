# -*- coding: utf-8 -*-
import pytest

from blackfennec_doubles.document_system.double_document_registry import DocumentRegistryMock
from blackfennec_doubles.document_system.mime_type.double_mime_type import MimeTypeMock
from blackfennec_doubles.document_system.resource_type.double_resource_type import ResourceTypeMock
from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec.document_system.document import Document


class TestDocument:
    @pytest.fixture
    def content(self):
        return StructureMock()

    @pytest.fixture
    def mime_type(self, content):
        return MimeTypeMock(imported_structure=content)

    @pytest.fixture
    def resource_type(self):
        return ResourceTypeMock()

    @pytest.fixture
    def document_registry(self):
        return DocumentRegistryMock()

    @pytest.fixture
    def document(self, document_registry, mime_type, resource_type):
        return Document(document_registry, mime_type, resource_type)

    def test_can_construct(self, document):
        assert document

    def test_get_content(self, content, document):
        assert content == document.content

    def test_does_register_document(self, document, document_registry):
        # registration is lazy
        document.content
        assert document_registry.registered_document == document

    def test_get_content_cached(self, document, mime_type, resource_type):
        content1 = document.content
        content2 = document.content
        assert content1 == content2
        assert resource_type.load_resource_count == 1
        assert mime_type.import_structure_count == 1

    def test_save(self, document, mime_type, resource_type):
        document.save()
        assert mime_type.export_structure_count == 1
