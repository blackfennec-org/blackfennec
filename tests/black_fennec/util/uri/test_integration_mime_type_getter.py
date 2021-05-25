import unittest

from uri import URI

from src.black_fennec.util.uri.uri_type import UriType
from src.black_fennec.util.uri.uri_import_service import UriImportService
from src.black_fennec.util.uri.uri_import_strategy_factory import UriImportStrategyFactory


class MimeTypeGetterIntegrationTestSuite(unittest.TestCase):

    def test_get_mimetype_online(self):
        uri = URI('https://jsonplaceholder.typicode.com/posts/1')
        uri_type = UriType.from_uri(uri)
        mime_type = UriImportService._get_mime_type(uri, uri_type, None)
        self.assertEqual(UriImportStrategyFactory.JSON_MIME_TYPE, mime_type)
