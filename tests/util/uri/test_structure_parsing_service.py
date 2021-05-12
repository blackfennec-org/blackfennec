import logging
import unittest

from doubles.double_dummy import Dummy
from doubles.util.json.double_json_reference_resolving_service import JsonReferenceResolvingServiceMock
from src.structure.boolean import Boolean
from src.structure.list import List
from src.structure.map import Map
from src.structure.number import Number
from src.structure.reference import Reference
from src.structure.string import String
from src.util.uri.structure_parsing_service import StructureParsingService


class StructureParsingServiceTestSuite(unittest.TestCase):
    def setUp(self):
        self.structure_parsing_service = StructureParsingService()

    def tearDown(self) -> None:
        self.structure_parsing_service: StructureParsingService = None

    def test_can_set_reference_resolving_service(self):
        reference_resolving_service = Dummy()
        self.structure_parsing_service.set_reference_resolving_service(reference_resolving_service)

    def test_can_parse_json_reference_to_reference(self):
        data = {'$ref': 'ref'}
        reference_resolving_service = JsonReferenceResolvingServiceMock()
        self.structure_parsing_service.set_reference_resolving_service(reference_resolving_service)
        result: Reference = self.structure_parsing_service.from_json(data)
        self.assertIsInstance(result, Reference)
        self.assertEqual(result._json_reference_resolve_service, reference_resolving_service)

    def test_can_parse_json_list_to_list(self):
        data = []
        result = self.structure_parsing_service.from_json(data)
        self.assertIsInstance(result, List)

    def test_can_parse_json_dict_to_map(self):
        data = {}
        result = self.structure_parsing_service.from_json(data)
        self.assertIsInstance(result, Map)

    def test_can_parse_json_list_to_string(self):
        data = 'Black Fennec'
        result = self.structure_parsing_service.from_json(data)
        self.assertIsInstance(result, String)

    def test_can_parse_json_int_to_number(self):
        data = 1337
        result = self.structure_parsing_service.from_json(data)
        self.assertIsInstance(result, Number)

    def test_can_parse_json_float_to_number(self):
        data = 3.141
        result = self.structure_parsing_service.from_json(data)
        self.assertIsInstance(result, Number)

    def test_can_parse_json_boolean_to_boolean(self):
        data = True
        result = self.structure_parsing_service.from_json(data)
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
        result = self.structure_parsing_service.from_json(data)
        self.assertIsInstance(result, Map)
        self.assertIsInstance(result['Tim'], Map)
        self.assertIsInstance(result['Tim']['firstname'], String)
        self.assertIsInstance(result['Tim']['age'], Number)
        self.assertIsInstance(result['Tim']['hobbies'], List)

    def test_can_parse_nested_list(self):
        data = {
            'continents': [
                {'identification': 'Asia', 'countries':
                    ['Russia', 'China', 'India', 'Mongolia']},
                {'identification': 'Africa', 'countries':
                    ['Nigeria', 'Ethiopia', 'Egypt', 'Kenya']},
                {'identification': 'Europe', 'countries':
                    ['Switzerland', 'Germany', 'France', 'Italy', 'Austria']}
            ]
        }
        result = self.structure_parsing_service.from_json(data)
        self.assertIsInstance(result['continents'], List)
        self.assertIsInstance(result['continents'][0]['identification'], String)
        self.assertIsInstance(result['continents'][0]['countries'], List)
        self.assertIsInstance(result['continents'][2]['identification'], String)
        self.assertIsInstance(result['continents'][2]['countries'], List)

    def test_throws_error_on_unknown_type(self):
        o = object()

        with self.assertRaises(TypeError):
            self.structure_parsing_service.from_json(o)

    def test_logs_error_on_unknown_type(self):
        o = object()

        with self.assertLogs(None, logging.ERROR):
            try:
                self.structure_parsing_service.from_json(o)
            except TypeError:
                pass

    def test_is_json_reference(self):
        reference = dict()
        reference[StructureParsingService.JSON_REFERENCE_KEY] = 'ref'
        self.assertTrue(StructureParsingService.is_json_reference(reference))

    def test_is_json_reference_with_no_json_reference(self):
        reference = dict()
        reference[StructureParsingService.JSON_REFERENCE_KEY + '$'] = 'ref'
        self.assertFalse(StructureParsingService.is_json_reference(reference))
