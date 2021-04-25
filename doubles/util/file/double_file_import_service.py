# -*- coding: utf-8 -*-

class FileImportServiceMock:
    def __init__(self):
        self.uri_str = None
        self.current_path = None
        self.mime_type = None
        self.load_count = 0

    def load(self, uri_str: str, current_path: str = None, mime_type: str = None):
        self.load_count += 1
        self.uri_str = uri_str
        self.current_path = current_path
        self.mime_type = mime_type