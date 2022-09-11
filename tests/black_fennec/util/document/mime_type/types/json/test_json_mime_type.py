# -*- coding: utf-8 -*-
import unittest
from io import StringIO

from doubles.black_fennec.util.document.mime_type.types.double_structure_encoding_service import \
    StructureEncodingServiceMock
from doubles.black_fennec.util.document.mime_type.types.double_structure_parsing_service import \
    StructureParsingServiceMock
from doubles.double_dummy import Dummy
from src.black_fennec.util.document.mime_type.types.json.json_mime_type import JsonMimeType


class JsonMimeTypeTestSuite(unittest.TestCase):

    def setUp(self) -> None:
        self.test_json_string = '{"test": "test"}'
        self.test_json = {'test': 'test'}
        self.test_json_file = StringIO(self.test_json_string)

    def tearDown(self) -> None:
        self.test_json_string = None
        self.test_json = None
        self.test_json_file = None

    def test_can_construct(self):
        JsonMimeType()

    def test_import_structure(self):
        structure_parsing_service = StructureParsingServiceMock()

        json_mime_type = JsonMimeType(
            structure_parsing_service=structure_parsing_service
        )
        json_mime_type.import_structure(self.test_json_file)

        self.assertEqual(structure_parsing_service.from_json_count, 1)

    def test_export_structure(self):
        structure_encoding_service = StructureEncodingServiceMock()

        json_mime_type = JsonMimeType(
            structure_encoding_service
        )
        structure_dummy = Dummy()
        json_mime_type.export_structure(structure_dummy)

        self.assertEqual(structure_encoding_service.encode_count, 1)
