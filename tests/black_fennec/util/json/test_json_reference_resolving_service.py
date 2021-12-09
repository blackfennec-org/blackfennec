import unittest

from uri import URI

from doubles.black_fennec.util.uri.double_uri_import_service import UriImportServiceMock
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.root_factory import RootFactory
from src.black_fennec.structure.string import String
from src.black_fennec.util.json.json_reference_resolving_service import JsonReferenceResolvingService


class JsonReferenceResolvingServiceTestSuite(unittest.TestCase):
    def test_can_construct(self):
        uri_import_service = UriImportServiceMock()
        JsonReferenceResolvingService(uri_import_service)

    def test_resolve_host_uri(self):
        data = {
            'key': String('value')
        }
        structure_map = Map(data)
        RootFactory.make_root(structure_map)

        uri_import_service = UriImportServiceMock(structure_map)
        resolving_service = JsonReferenceResolvingService(uri_import_service)
        result = resolving_service.resolve(URI('https://test.test'), structure_map)
        self.assertEqual(result.value, structure_map.value)

    def test_resolve_absolute_uri(self):
        data = {
            'key': String('value')
        }
        structure_map = Map(data)
        RootFactory.make_root(structure_map)

        uri_import_service = UriImportServiceMock(structure_map)
        resolving_service = JsonReferenceResolvingService(uri_import_service)
        result = resolving_service.resolve(URI('C:/test.json'), structure_map)
        self.assertEqual(result.value, structure_map.value)

    def test_resolve_relative_uri(self):
        data = {
            'key': String('value')
        }
        structure_map = Map(data)
        RootFactory.make_root(structure_map)

        uri_import_service = UriImportServiceMock(structure_map)
        resolving_service = JsonReferenceResolvingService(uri_import_service)
        result = resolving_service.resolve(URI('./test.json'), structure_map)
        self.assertEqual(result.value, structure_map.value)

    def test_resolve_relative_json_pointer(self):
        data = {
            'key': String('value')
        }
        structure_map = Map(data)
        RootFactory.make_root(structure_map)

        uri_import_service = UriImportServiceMock(structure_map)
        resolving_service = JsonReferenceResolvingService(uri_import_service)
        result = resolving_service.resolve(URI('1'), structure_map.value['key'])
        self.assertEqual(result.value, structure_map.value)

    def test_resolve_current_location_uri(self):
        data = {
            'key': String('value')
        }
        structure_map = Map(data)
        RootFactory.make_root(structure_map)

        uri_import_service = UriImportServiceMock(structure_map)
        resolving_service = JsonReferenceResolvingService(uri_import_service)
        result = resolving_service.resolve(URI('#key'), structure_map)
        self.assertEqual(result.value, structure_map.value['key'].value)

    def test_resolve_caching(self):
        data = {
            'key': String('value')
        }
        structure_map = Map(data)
        RootFactory.make_root(structure_map)

        uri_import_service = UriImportServiceMock(structure_map)
        resolving_service = JsonReferenceResolvingService(uri_import_service)
        resolving_service.resolve(URI('https://test.test'), structure_map)
        result = resolving_service.resolve(URI('https://test.test'), None)
        self.assertEqual(result.value, structure_map.value)
