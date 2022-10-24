# -*- coding: utf-8 -*-
import contextlib
from io import StringIO
from typing import IO, List

from blackfennec.document_system.document import Document
from blackfennec.document_system.resource_type.resource_type import ResourceType


class ResourceTypeMock(ResourceType):
    def __init__(self, protocols=None, loaded_resource=None):
        self._protocols = protocols or ['']
        self._loaded_resource = loaded_resource or StringIO()
        self.loaded_resource_document_parameter = None
        self.load_resource_count = 0

    @property
    def protocols(self) -> List[str]:
        return self._protocols

    @contextlib.contextmanager
    def load_resource(self, document: Document, mode: str) -> IO:
        self.load_resource_count += 1
        self.loaded_resource_document_parameter = document
        yield self._loaded_resource
