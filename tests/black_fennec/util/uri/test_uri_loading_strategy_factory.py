import unittest

from uri import URI

from src.black_fennec.util.uri.uri_loading_strategy_factory import UriLoadingStrategyFactory


class UriLoadingStrategyFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        UriLoadingStrategyFactory()

    def test_can_create_with_host_uri(self):
        factory = UriLoadingStrategyFactory()
        uri = URI('https://test.com')
        factory.create(uri)

    def test_can_create_with_absolute_uri(self):
        factory = UriLoadingStrategyFactory()
        uri = URI('C:/test.json')
        factory.create(uri)

    def test_can_create_with_relative_uri(self):
        factory = UriLoadingStrategyFactory()
        uri = URI('./test.json')
        factory.create(uri)

    def test_can_create_with_current_location_uri(self):
        factory = UriLoadingStrategyFactory()
        uri = URI('.')
        with self.assertRaises(NotImplementedError):
            factory.create(uri)
