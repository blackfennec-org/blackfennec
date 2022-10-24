# -*- coding: utf-8 -*-
import pytest

from blackfennec_doubles.structure.double_root_factory import RootFactoryMock
from blackfennec_doubles.document_system.mime_type.double_mime_type import MimeTypeMock
from blackfennec_doubles.document_system.resource_type.double_resource_type import ResourceTypeMock
from blackfennec.document_system.document import Document


class TestDocument:
    @pytest.fixture
    def mime_type(self):
        return MimeTypeMock()

    @pytest.fixture
    def resource_type(self):
        return ResourceTypeMock()

    @pytest.fixture
    def root_factory(self):
        return RootFactoryMock()

    @pytest.fixture
    def document(self, mime_type, resource_type, root_factory):
        return Document(mime_type, resource_type, root_factory)

    def test_can_construct(self, document):
        pass

    def test_get_content(self, document, mime_type, resource_type, root_factory):
        content = document.content
        assert root_factory.make_root_document_parameter == document

    def test_get_content_cached(self, document, mime_type, resource_type):
        content1 = document.content
        content2 = document.content
        assert content1 == content2
        assert resource_type.load_resource_count == 1
        assert mime_type.import_structure_count == 1

    def test_save(self, document, mime_type, resource_type):
        document.save()
        assert mime_type.export_structure_count == 1
