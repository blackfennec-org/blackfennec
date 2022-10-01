# -*- coding: utf-8 -*-
import contextlib
import os
from typing import IO, List
from urllib.parse import urlparse

from src.black_fennec.util.document.document import Document
from src.black_fennec.util.document.resource_type.resource_type import ResourceType


class FileResourceType(ResourceType):
    @property
    def protocols(self) -> List[str]:
        return [
            'file'
        ]

    @contextlib.contextmanager
    def load_resource(self, document: Document) -> IO:
        """Load the resource

        Arguments:
            document (Document): document to load
        Returns:
            IO: loaded resource
        """
        parsed_uri = urlparse(document.uri)
        document_path = parsed_uri.path

        if not os.path.isabs(document_path):
            parsed_location = urlparse(document.location)
            current_path = parsed_location.path
            document_path = os.path.join(current_path, parsed_uri.path)

        file = None
        try:
            file = open(document_path, 'r+')
            yield file
        finally:
            if file is not None:
                file.close()
