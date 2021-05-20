import unittest

from src.black_fennec.util.uri.uri_import_strategy_factory import UriImportStrategyFactory


class UriImportStrategyFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        UriImportStrategyFactory()

    def test_can_create(self):
        factory = UriImportStrategyFactory()
        factory.create(UriImportStrategyFactory.JSON_MIME_TYPE)

    def test_create_with_unimplemented_type(self):
        factory = UriImportStrategyFactory()
        with self.assertRaises(NotImplementedError):
            factory.create('non-existent-mime-type')