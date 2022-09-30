import json
import unittest

from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.util.document.mime_type.types.json.structure_encoding_service import StructureEncodingService
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.string import String


class StructureEncodingServiceTestSuite(unittest.TestCase):

    def test_list_to_json_string(self):
        black_fennec_obj = List([String('identification')])
        expected = """[
    "identification"
]"""
        json_string = json.dumps(
            black_fennec_obj,
            indent=4,
            cls=StructureEncodingService)
        self.assertEqual(expected, json_string)

    def test_Map_to_json_string(self):
        black_fennec_obj = Map({'identification': String('Timo')})
        expected = """{
    "identification": "Timo"
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
