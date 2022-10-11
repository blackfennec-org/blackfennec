# -*- coding: utf-8 -*-
import contextlib
from typing import List
from urllib.parse import urlparse

from src.black_fennec.document_system.document import Document
from src.black_fennec.document_system.resource_type.resource_type import ResourceType


class BFTypeResourceType(ResourceType):
    def __init__(self, type_registry):
        self._type_registry = type_registry

    @property
    def protocols(self) -> List[str]:
        return [
            'bftype'
        ]

    @contextlib.contextmanager
    def load_resource(self, document: Document):
        """Load the resource

        Arguments:
            document (Document): document to load
        Returns:
            IO: loaded resource
        """
        parsed_uri = urlparse(document.uri)
        type_name = parsed_uri.path or parsed_uri.netloc

        for type in self._type_registry.types:
            if type.name == type_name:
                yield type.subject
                return
        
        raise KeyError(f'Could not find type with name: {type_name}')

    def guess_mime_type(self, uri: str):
        return 'black_fennec/in_memory'
