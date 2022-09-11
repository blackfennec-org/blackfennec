# -*- coding: utf-8 -*-

class StructureEncodingServiceMock:
    def __init__(self, encode_result=None):
        self.encode_count = 0
        self.raw = None
        self._encode_result = encode_result

    def encode(self, raw):
        self.encode_count += 1
        self.raw = raw
        return self._encode_result
