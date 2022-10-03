# -*- coding: utf-8 -*-
from doubles.black_fennec.document_system.mime_type.double_mime_type_registry import MimeTypeRegistryMock
from doubles.black_fennec.document_system.resource_type.double_resource_type_registry import ResourceTypeRegistryMock


class DocumentFactoryMock:
    def __init__(self, mime_type_registry=None, resource_type_registry=None, create_return=None):
        self.mime_type_registry = mime_type_registry or MimeTypeRegistryMock()
        self.resource_type_registry = resource_type_registry or ResourceTypeRegistryMock()
        self._create_return = create_return

        self.create_count = 0

    def create(
            self,
            uri: str,
            resource_type: str = None,
            mime_type: str = None,
            location: str = None
    ):
        self.create_count += 1
        return self._create_return
