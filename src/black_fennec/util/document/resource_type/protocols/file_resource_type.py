# -*- coding: utf-8 -*-
import os
import contextlib
from typing import IO
from uri import URI

from src.black_fennec.util.document.document import Document
from src.black_fennec.util.document.resource_type.resource_type import ResourceType


class FileResourceType(ResourceType):
    PROTOCOLS = [
        'file'
    ]

    @contextlib.contextmanager
    def load_resource(self, document: Document) -> IO:
        current_path = URI(document.location).path
        document_path = URI(document.uri).path
        if not os.path.isabs(document_path):
            document_path = os.path.join(current_path, URI(document.uri).path)

        file = None
        try:
            file = open(document_path, 'r')
            yield file
        finally:
            if file is not None:
                file.close()
