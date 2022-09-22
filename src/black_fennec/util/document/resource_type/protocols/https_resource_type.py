# -*- coding: utf-8 -*-
import contextlib
from typing import IO, List

from src.black_fennec.util.document.resource_type.resource_type import ResourceType
import urllib.request as req


class HttpsResourceType(ResourceType):

    @property
    def protocols(cls) -> List[str]:
        return [
            'http',
            'https'
        ]

    @contextlib.contextmanager
    def load_resource(self, document: 'Document') -> IO:
        path, response = req.urlretrieve(document.uri)
        file = None
        try:
            file = open(path, 'r')
            yield file
        finally:
            if file is not None:
                file.close()
