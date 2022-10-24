# -*- coding: utf-8 -*-
from blackfennec_doubles.double_dummy import Dummy


class DocumentMock:
    def __init__(self, mime_type=None, resource_type=None, uri: str = None, location: str = None, content=None):
        self.uri = uri
        self.location = location
        self.mime_type = mime_type or Dummy()
        self.resource_type = resource_type or Dummy()
        self._content = content

        self.load_content_count = 0

    @property
    def content(self):
        self.load_content_count += 1
        return self._content
