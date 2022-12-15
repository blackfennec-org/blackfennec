# -*- coding: utf-8 -*-


class MimeTypeRegistryMock:

    def __init__(self, mime_types=None):
        if mime_types is None:
            mime_types = dict()
        self._mime_types = mime_types
        self.mime_types_getter_count = 0

        self.register_mime_type_count = 0
        self.register_mime_type_last_mime_type = None
        self.register_mime_type_last_mime_type_key = None

        self.deregister_mime_type_count = 0
        self.deregister_mime_type_last_mime_type_key = None

    @property
    def mime_types(self):
        self.mime_types_getter_count += 1
        return self._mime_types

    @mime_types.setter
    def mime_types(self, mime_types):
        self._mime_types = mime_types

    def register_mime_type(self, mime_key, mime_type):
        self.register_mime_type_last_mime_type = mime_type
        self.register_mime_type_last_mime_type_key = mime_key
        self.register_mime_type_count += 1

    def deregister_mime_type(self, mime_type_key):
        self.deregister_mime_type_last_mime_type_key = mime_type_key
        self.deregister_mime_type_count += 1
