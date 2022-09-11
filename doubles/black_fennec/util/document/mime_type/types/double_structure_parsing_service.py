# -*- coding: utf-8 -*-

class StructureParsingServiceMock:
    def __init__(self, from_json_result=None):
        self.raw = None
        self.reference_resolving_service = None
        self.from_json_count = 0
        self.reference_resolving_service_set_count = 0
        self._from_json_result = from_json_result

    def set_reference_resolving_service(self, reference_resolving_service):
        self.reference_resolving_service_set_count += 1
        self.reference_resolving_service = reference_resolving_service

    def from_json(self, raw):
        self.from_json_count += 1
        self.raw = raw
        return self._from_json_result
