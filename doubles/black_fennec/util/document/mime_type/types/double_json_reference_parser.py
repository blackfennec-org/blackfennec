# -*- coding: utf-8 -*-
from src.black_fennec.structure.reference_navigation.navigator import Navigator


class JsonReferenceParserMock:
    def __init__(self, parse_result=None):
        self.parse_count = 0
        self.parse_parameter_raw = None
        self._parse_result = parse_result

    def parse(self, raw: dict) -> list[Navigator]:
        self.parse_parameter_raw = raw
        self.parse_count += 1
        return self._parse_result
