# -*- coding: utf-8 -*-
from src.black_fennec.structure.reference_navigation.navigator import Navigator


class JsonPointerParserMock:
    def __init__(self, parse_absolute_pointer=None, parse_relative_pointer=None):
        self.parse_absolute_pointer_count = 0
        self.parse_absolute_pointer_parameter_json_pointer = None
        self._parse_absoulte_pointer_result = parse_absolute_pointer
        self.parse_relative_pointer_count = 0
        self.parse_relative_pointer_parameter_json_pointer = None
        self._parse_relative_pointer_result = parse_relative_pointer

    def parse_absolute_pointer(self, json_pointer: str) -> list[Navigator]:
        self.parse_absolute_pointer_parameter_json_pointer = json_pointer
        self.parse_absolute_pointer_count += 1
        return self._parse_absoulte_pointer_result

    def parse_relative_pointer(self, json_pointer: str) -> list[Navigator]:
        self.parse_relative_pointer_parameter_json_pointer = json_pointer
        self.parse_relative_pointer_count += 1
        return self._parse_relative_pointer_result
