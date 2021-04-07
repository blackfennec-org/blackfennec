import unittest
import logging
from src.core.boolean import Boolean
from src.core.json_parser import JsonParser
from src.core.list import List
from src.core.map import Map
from src.core.number import Number
from src.core.string import String


class JsonParserTestSuite(unittest.TestCase):
    def test_can_parse_json_list_to_list(self):
        data = []
        result = JsonParser.from_json(data)
        self.assertIsInstance(result, List)

    def test_can_parse_json_dict_to_map(self):
        data = {}
        result = JsonParser.from_json(data)
        self.assertIsInstance(result, Map)

    def test_can_parse_json_list_to_string(self):
        data = 'Black Fennec'
        result = JsonParser.from_json(data)
        self.assertIsInstance(result, String)

    def test_can_parse_json_int_to_number(self):
        data = 1337
        result = JsonParser.from_json(data)
        self.assertIsInstance(result, Number)

    def test_can_parse_json_float_to_number(self):
        data = 3.141
        result = JsonParser.from_json(data)
        self.assertIsInstance(result, Number)

    def test_can_parse_json_boolean_to_boolean(self):
        data = True
        result = JsonParser.from_json(data)
        self.assertIsInstance(result, Boolean)

    def test_can_parse_person(self):
        data = {
            'Tim': {
                'firstname': 'Timo',
                'lastname': 'Turbo',
                'age': 42,
                'hobbies': ['climbing', 'soccer']
            }
        }
        result = JsonParser.from_json(data)
        self.assertIsInstance(result, Map)
        self.assertIsInstance(result['Tim'], Map)
        self.assertIsInstance(result['Tim']['firstname'], String)
        self.assertIsInstance(result['Tim']['age'], Number)
        self.assertIsInstance(result['Tim']['hobbies'], List)

    def test_can_parse_nested_list(self):
        data = {
            'continents': [
                {'name': 'Asia', 'countries':
                    ['Russia', 'China', 'India', 'Mongolia']},
                {'name': 'Africa', 'countries':
                    ['Nigeria', 'Ethiopia', 'Egypt', 'Kenya']},
                {'name': 'Europe', 'countries':
                    ['Switzerland', 'Germany', 'France', 'Italy', 'Austria']}
            ]
        }
        result = JsonParser.from_json(data)
        self.assertIsInstance(result['continents'], List)
        self.assertIsInstance(result['continents'][0]['name'], String)
        self.assertIsInstance(result['continents'][0]['countries'], List)
        self.assertIsInstance(result['continents'][2]['name'], String)
        self.assertIsInstance(result['continents'][2]['countries'], List)

    def test_throws_error_on_unknown_type(self):
        o = object()

        with self.assertRaises(TypeError):
            JsonParser.from_json(o)

    def test_logs_error_on_unknown_type(self):
        o = object()

        with self.assertLogs(None, logging.ERROR):
            try:
                JsonParser.from_json(o)
            except TypeError:
                pass
