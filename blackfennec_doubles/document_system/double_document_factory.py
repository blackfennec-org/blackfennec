# -*- coding: utf-8 -*-
from blackfennec_doubles.document_system.mime_type.double_mime_type_registry import MimeTypeRegistryMock
from blackfennec_doubles.document_system.resource_type.double_resource_type_registry import ResourceTypeRegistryMock


class DocumentFactoryMock:
    def __init__(
            self, 
            mime_type_registry=None, 
            resource_type_registry=None, 
            document=None):
        self.mime_type_registry = mime_type_registry or MimeTypeRegistryMock()
        self.resource_type_registry = resource_type_registry or ResourceTypeRegistryMock()
        self._document = document

        self.create_count = 0
        self.get_document_count = 0

    def create(
            self,
            uri: str,
            resource_type: str = None,
            mime_type: str = None,
            location: str = None
    ):
        self.create_count += 1
        return self._document

    def get_document(self, structure):
        self.get_document_count += 1
        return self._document
