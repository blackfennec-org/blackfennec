# -*- coding: utf-8 -*-
import contextlib
import os
from pathlib import Path
from typing import IO, List
from urllib.parse import urlparse

from blackfennec.document_system.document import Document
from blackfennec.document_system.resource_type.resource_type import ResourceType


class FileResourceType(ResourceType):
    @property
    def protocols(self) -> List[str]:
        return [
            'file'
        ]

    @contextlib.contextmanager
    def load_resource(self, document: Document, mode: str) -> IO:
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
        if not os.path.exists(document_path):
            Path(document_path).touch()
        try:
            file = open(document_path, mode)
            yield file
        finally:
            if file is not None:
                file.close()
