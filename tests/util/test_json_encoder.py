import json
import unittest

from src.structure.boolean import Boolean
from src.util.file.structure_encoding_service import StructureEncodingService
from src.structure.list import List
from src.structure.map import Map
from src.structure.number import Number
from src.structure.string import String


class StructureEncoderTestSuite(unittest.TestCase):

    def test_list_to_json_string(self):
        black_fennec_obj = List([String('name')])
        expected = """[
    "name"
]"""
        json_string = json.dumps(
            black_fennec_obj,
            indent=4,
            cls=StructureEncodingService)
        self.assertEqual(expected, json_string)

    def test_Map_to_json_string(self):
        black_fennec_obj = Map({'name': String('Timo')})
        expected = """{
    "name": "Timo"
}"""
        json_string = json.dumps(
            black_fennec_obj,
            indent=4,
            cls=StructureEncodingService)
        self.assertEqual(expected, json_string)

    def test_string_to_json_string(self):
        black_fennec_obj = String('Turbo')
        expected = '"Turbo"'
        json_string = json.dumps(
            black_fennec_obj,
            indent=4,
            cls=StructureEncodingService)
        self.assertEqual(expected, json_string)

    def test_number_to_json_string(self):
        black_fennec_obj = Number(42)
        expected = '42'
        json_string = json.dumps(
            black_fennec_obj,
            indent=4,
            cls=StructureEncodingService)
        self.assertEqual(expected, json_string)

    def test_boolean_to_json_string(self):
        black_fennec_obj = Boolean(True)
        expected = 'true'
        json_string = json.dumps(
            black_fennec_obj,
            indent=4,
            cls=StructureEncodingService)
        self.assertEqual(expected, json_string)
