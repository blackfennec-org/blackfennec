import json
import os
import tempfile
import unittest
from urllib import request as req

from src.util.uri.structure_parsing_service import StructureParsingService
from src.util.uri.uri_import_service import UriImportService
from src.util.uri.uri_import_strategy_factory import UriImportStrategyFactory
from src.util.uri.uri_loading_strategy_factory import UriLoadingStrategyFactory


class UriImportServiceIntegrationTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.host_uri = "http://echo.jsontest.com/key/value/"
        self.tmp_file = tempfile.mktemp()
        req.urlretrieve(self.host_uri, self.tmp_file)
        parser = StructureParsingService()
        loader_factory = UriLoadingStrategyFactory()
        import_factory = UriImportStrategyFactory()
        with open(self.tmp_file, 'r') as file:
            raw = json.load(file)
            self.black_fennec_obj = parser.from_json(raw)
            self.import_service = UriImportService(parser, loader_factory, import_factory)

    def tearDown(self) -> None:
        pass

    def test_load_file_from_relative_uri(self):
        current_path = os.path.dirname(self.tmp_file)
        path = os.path.relpath(self.tmp_file, current_path)
        structure = self.import_service.load(path, self.tmp_file, UriImportStrategyFactory.JSON_MIME_TYPE)
        self.assertEqual(self.black_fennec_obj, structure)

    def test_load_file_from_absolute_uri(self):
        path = os.path.abspath(self.tmp_file)
        structure = self.import_service.load(path, None, UriImportStrategyFactory.JSON_MIME_TYPE)
        self.assertEqual(self.black_fennec_obj, structure)

    def test_load_file_from_host_uri(self):
        structure = self.import_service.load(self.host_uri)
        self.assertEqual(self.black_fennec_obj, structure)
