# -*- coding: utf-8 -*-
from typing import Type, Optional

from blackfennec.document_system.document import Document
from blackfennec.document_system.document_registry import DocumentRegistry
from blackfennec.document_system.mime_type.mime_type import MimeType
from blackfennec.document_system.mime_type.mime_type_registry import MimeTypeRegistry
from blackfennec.document_system.resource_type.resource_type import ResourceType
from blackfennec.document_system.resource_type.resource_type_registry import ResourceTypeRegistry


class DocumentFactory:
    def __init__(
            self,
            document_registry: DocumentRegistry,
            resource_type_registry: ResourceTypeRegistry,
            mime_type_registry: MimeTypeRegistry,
            document_type: Type[Document] = Document
    ):
        self._document_registry = document_registry
        self._mime_type_registry = mime_type_registry
        self._resource_type_registry = resource_type_registry
        self._document_type = document_type

    def create(
            self,
            uri: str,
            resource_type_id: Optional[str] = None,
            mime_type_id: Optional[str] = None,
            location: Optional[str] = None
    ) -> Document:
        if not resource_type_id:
            resource_type_id = ResourceType.try_determine_resource_type(uri)
        resource_type = self._resource_type_registry.resource_types[resource_type_id]

        if not mime_type_id:
            mime_type_id = MimeType.try_determine_mime_type(uri, resource_type)
        mime_type = self._mime_type_registry.mime_types[mime_type_id]

        return self._document_type(
            self._document_registry, 
            mime_type, 
            resource_type, 
            uri=uri, 
            location=location)

    def get_document(self, structure) -> Document:
        return self._document_registry.get_document(structure)
