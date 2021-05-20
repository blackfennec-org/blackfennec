# -*- coding: utf-8 -*-

class JsonReferenceResolvingServiceMock:
    def __init__(self, file_import_service=None, resolve_return=None):
        self.file_import_service = file_import_service
        self.reference = None
        self.source = None
        self.resolve_count = 0
        self.resolve_return = resolve_return

    def resolve(self, reference: str, source=None):
        self.resolve_count += 1
        self.reference = reference
        self.source = source
        return self.resolve_return
