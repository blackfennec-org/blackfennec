import json
import unittest

from src.core.types.boolean import Boolean
from src.core.json_encoder import JsonEncoder
from src.core.types.list import List
from src.core.types.map import Map
from src.core.types.number import Number
from src.core.types.string import String


class JsonEncoderTestSuite(unittest.TestCase):

    def test_list_to_json_string(self):
        black_fennec_obj = List([String('name')])
        expected = """[
    "name"
]"""
        json_string = json.dumps(
            black_fennec_obj,
            indent=4,
            cls=JsonEncoder)
        self.assertEqual(expected, json_string)

    def test_Map_to_json_string(self):
        black_fennec_obj = Map({'name': String('Timo')})
        expected = """{
    "name": "Timo"
}"""
        json_string = json.dumps(
            black_fennec_obj,
            indent=4,
            cls=JsonEncoder)
        self.assertEqual(expected, json_string)

    def test_string_to_json_string(self):
        black_fennec_obj = String('Turbo')
        expected = '"Turbo"'
        json_string = json.dumps(
            black_fennec_obj,
            indent=4,
            cls=JsonEncoder)
        self.assertEqual(expected, json_string)

    def test_number_to_json_string(self):
        black_fennec_obj = Number(42)
        expected = '42'
        json_string = json.dumps(
            black_fennec_obj,
            indent=4,
            cls=JsonEncoder)
        self.assertEqual(expected, json_string)

    def test_boolean_to_json_string(self):
        black_fennec_obj = Boolean(True)
        expected = 'true'
        json_string = json.dumps(
            black_fennec_obj,
            indent=4,
            cls=JsonEncoder)
        self.assertEqual(expected, json_string)
