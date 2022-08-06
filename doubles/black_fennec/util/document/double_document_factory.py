# -*- coding: utf-8 -*-
from doubles.black_fennec.util.document.mime_type.double_mime_type_registry import MimeTypeRegistryMock
from doubles.black_fennec.util.document.resource_type.resource_type_registry import ResourceTypeRegistryMock
from doubles.double_dummy import Dummy


class DocumentFactoryMock:
    def __init__(self, mime_type_registry=None, resource_type_registry=None, create_return=None):
        self.mime_type_registry = mime_type_registry or MimeTypeRegistryMock()
        self.resource_type_registry = resource_type_registry or ResourceTypeRegistryMock()
        self._create_return = create_return

        self.create_count = 0

    def create(self, uri: str, resource_type: str, mime_type: str, location: str = None):
        self.create_count += 1
        return self._create_return
