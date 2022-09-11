# -*- coding: utf-8 -*-
from typing import Type

from src.black_fennec.util.document.document import Document
from src.black_fennec.util.document.mime_type.mime_type_registry import MimeTypeRegistry
from src.black_fennec.util.document.resource_type.resource_type_registry import ResourceTypeRegistry


class DocumentFactory:
    def __init__(
            self,
            resource_type_registry: ResourceTypeRegistry,
            mime_type_registry: MimeTypeRegistry,
            document_type: Type[Document] = Document
    ):
        self._mime_type_registry = mime_type_registry
        self._resource_type_registry = resource_type_registry
        self._document_type = document_type

    def create(self, uri: str, resource_type: str, mime_type: str, location: str = None) -> Document:
        resource_type = self._resource_type_registry.resource_types[resource_type]
        mime_type = self._mime_type_registry.mime_types[mime_type]

        return self._document_type(mime_type, resource_type, uri=uri, location=location)
