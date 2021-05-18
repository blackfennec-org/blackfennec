# -*- coding: utf-8 -*-
from doubles.structure.double_map import MapMock
from src.extension.extension_status import ExtensionStatus


class ExtensionMock:
    def __init__(self, source_map = None, status=None):
        self.underlay = source_map if source_map else MapMock()
        self.status = status if status else (ExtensionStatus.NOT_LOADED, None)
        self.load_count = 0
        self.unload_count = 0
        self.extension_api = None

    def load(self, extension_api):
        self.load_count += 1
        self.extension_api = extension_api

    def unload(self, extension_api):
        self.unload_count += 1
        self.extension_api = extension_api
