import logging
import unittest

from doubles.double_dummy import Dummy
from doubles.black_fennec.util.json.double_json_reference_resolving_service import JsonReferenceResolvingServiceMock
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.string import String
from src.black_fennec.util.document.mime_type.types.structure_parsing_service import StructureParsingService


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
        self.assertIsInstance(result.value['Tim'], Map)
        self.assertIsInstance(result.value['Tim'].value['firstname'], String)
        self.assertIsInstance(result.value['Tim'].value['age'], Number)
        self.assertIsInstance(result.value['Tim'].value['hobbies'], List)

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
        self.assertIsInstance(result.value['continents'], List)
        self.assertIsInstance(result.value['continents'].value[0].value['identification'], String)
        self.assertIsInstance(result.value['continents'].value[0].value['countries'], List)
        self.assertIsInstance(result.value['continents'].value[2].value['identification'], String)
        self.assertIsInstance(result.value['continents'].value[2].value['countries'], List)

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
