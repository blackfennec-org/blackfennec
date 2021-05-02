import unittest

from doubles.util.uri.double_uri_import_service import UriImportServiceMock
from src.structure.map import Map
from src.structure.root import Root
from src.structure.string import String
from src.util.json.json_reference_resolving_service import JsonReferenceResolvingService


class JsonReferenceResolvingServiceTestSuite(unittest.TestCase):
    def test_can_construct(self):
        uri_import_service = UriImportServiceMock()
        JsonReferenceResolvingService(uri_import_service)

    def test_resolve_host_uri(self):
        data = {
            'key': String('value')
        }
        map = Map(data)
        map.parent = Root(map)

        uri_import_service = UriImportServiceMock(map)
        resolving_service = JsonReferenceResolvingService(uri_import_service)
        result = resolving_service.resolve('https://test.test', map)
        self.assertEqual(result, map)

    def test_resolve_absolute_uri(self):
        data = {
            'key': String('value')
        }
        map = Map(data)
        map.parent = Root(map)

        uri_import_service = UriImportServiceMock(map)
        resolving_service = JsonReferenceResolvingService(uri_import_service)
        result = resolving_service.resolve('C:/test.json', map)
        self.assertEqual(result, map)

    def test_resolve_relative_uri(self):
        data = {
            'key': String('value')
        }
        map = Map(data)
        map.parent = Root(map)

        uri_import_service = UriImportServiceMock(map)
        resolving_service = JsonReferenceResolvingService(uri_import_service)
        result = resolving_service.resolve('./test.json', map)
        self.assertEqual(result, map)

    def test_resolve_relative_json_pointer(self):
        data = {
            'key': String('value')
        }
        map = Map(data)
        map.parent = Root(map)

        uri_import_service = UriImportServiceMock(map)
        resolving_service = JsonReferenceResolvingService(uri_import_service)
        result = resolving_service.resolve('1', map['key'])
        self.assertEqual(result, map)

    def test_resolve_current_location_uri(self):
        data = {
            'key': String('value')
        }
        map = Map(data)
        map.parent = Root(map)

        uri_import_service = UriImportServiceMock(map)
        resolving_service = JsonReferenceResolvingService(uri_import_service)
        result = resolving_service.resolve('#key', map)
        self.assertEqual(result, map['key'])

    def test_resolve_caching(self):
        data = {
            'key': String('value')
        }
        map = Map(data)
        map.parent = Root(map)

        uri_import_service = UriImportServiceMock(map)
        resolving_service = JsonReferenceResolvingService(uri_import_service)
        resolving_service.resolve('https://test.test', map)
        result = resolving_service.resolve('https://test.test', None)
        self.assertEqual(result, map)
