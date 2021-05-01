# -*- coding: utf-8 -*-
import tempfile
import unittest

from uri import URI

from doubles.double_dummy import Dummy
from doubles.structure.double_map import MapMock
from doubles.util.file.double_uri_import_strategy_factory import UriImportStrategyFactoryMock
from doubles.util.file.double_structure_parsing_service import StructureParsingServiceMock
from doubles.util.file.double_uri_loading_strategy_factory import UriLoadingStrategyFactoryMock
from src.util.uri.uri_type import UriType
from src.util.uri.uri_import_service import UriImportService
from src.util.uri.uri_import_strategy_factory import UriImportStrategyFactory


class UriImportServiceTestSuite(unittest.TestCase):
    def test_can_construct(self):
        UriImportService(Dummy(), Dummy(), Dummy())

    def test_load(self):
        uri = URI('http://test.test/test.json')
        tmp_file = tempfile.TemporaryFile()
        loading_strategy_factory = UriLoadingStrategyFactoryMock(tmp_file)
        raw = dict()
        import_strategy_factory = UriImportStrategyFactoryMock(raw)
        underlay = MapMock()
        structure_parser = StructureParsingServiceMock(underlay)
        uri_import_service = \
            UriImportService(
                structure_parser,
                loading_strategy_factory,
                import_strategy_factory
            )
        result = uri_import_service.load(str(uri))

        self.assertEqual(uri, loading_strategy_factory.uri)
        self.assertEqual(tmp_file, import_strategy_factory.file_pointer)
        self.assertEqual(raw, structure_parser.raw)
        self.assertEqual(underlay, result)

    def test_load_from_cache(self):
        uri = URI('./test.json')
        uri_identifier = UriImportService._uri_identification(uri, UriType.RELATIVE_PATH, UriImportStrategyFactory.JSON_MIME_TYPE)
        underlay = MapMock()
        cache = dict()
        cache[uri_identifier] = underlay
        loading_strategy_factory = UriLoadingStrategyFactoryMock()
        import_strategy_factory = UriImportStrategyFactoryMock()
        structure_parser = StructureParsingServiceMock()
        uri_import_service = \
            UriImportService(
                structure_parser,
                loading_strategy_factory,
                import_strategy_factory,
                cache
            )
        result = uri_import_service.load(str(uri), mime_type=UriImportStrategyFactory.JSON_MIME_TYPE)

        self.assertIsNone(loading_strategy_factory.uri)
        self.assertIsNone(import_strategy_factory.file_pointer)
        self.assertIsNone(structure_parser.raw)
        self.assertEqual(underlay, result)

    def test_load_without_identifiable_mimetype(self):
        uri = URI('./test')
        underlay = MapMock()
        loading_strategy_factory = UriLoadingStrategyFactoryMock()
        import_strategy_factory = UriImportStrategyFactoryMock()
        structure_parser = StructureParsingServiceMock()
        uri_import_service = \
            UriImportService(
                structure_parser,
                loading_strategy_factory,
                import_strategy_factory,
            )
        with self.assertRaises(ValueError):
            uri_import_service.load(str(uri), mime_type=None)
