import unittest

from uri import URI

from doubles.black_fennec.util.document.double_document import DocumentMock
from doubles.black_fennec.util.document.double_document_factory import DocumentFactoryMock
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.root_factory import RootFactory
from src.black_fennec.structure.string import String
from src.black_fennec.util.json.json_reference_resolving_service import JsonReferenceResolvingService


class JsonReferenceResolvingServiceTestSuite(unittest.TestCase):
    def setUp(self) -> None:
        data = {
            'key': String('value')
        }
        self.structure_map = Map(data)
        self.document = DocumentMock(content=self.structure_map)
        self.document_factory = DocumentFactoryMock(create_return=self.document)

        RootFactory.make_root(self.structure_map, self.document)

    def tearDown(self) -> None:
        self.document = None
        self.document_factory = None

    def test_can_construct(self):
        JsonReferenceResolvingService(self.document_factory)

    def test_resolve_host_uri(self):
        uri = 'https://test.test/test.json'
        self.document.uri = uri

        resolving_service = JsonReferenceResolvingService(self.document_factory)
        result = resolving_service.resolve(uri, self.structure_map)
        self.assertEqual(result.value, self.structure_map.value)

    def test_resolve_absolute_uri(self):
        uri = 'C:/test.json'
        self.document.uri = uri

        resolving_service = JsonReferenceResolvingService(self.document_factory)
        result = resolving_service.resolve(uri, self.structure_map)
        self.assertEqual(result.value, self.structure_map.value)

    def test_resolve_relative_uri(self):
        uri = './test.json'
        self.document.uri = uri

        resolving_service = JsonReferenceResolvingService(self.document_factory)
        result = resolving_service.resolve(uri, self.structure_map)
        self.assertEqual(result.value, self.structure_map.value)

    def test_resolve_relative_json_pointer(self):
        resolving_service = JsonReferenceResolvingService(self.document_factory)
        result = resolving_service.resolve('1', self.structure_map.value['key'])
        self.assertEqual(result.value, self.structure_map.value)

    def test_resolve_current_location_uri(self):
        resolving_service = JsonReferenceResolvingService(self.document_factory)
        result = resolving_service.resolve('#key', self.structure_map)
        self.assertEqual(result.value, self.structure_map.value['key'].value)

    def test_resolve_caching(self):
        uri = 'https://test.test/test.json'
        self.document.uri = uri

        resolving_service = JsonReferenceResolvingService(self.document_factory)
        resolving_service.resolve(uri, self.structure_map)
        result = resolving_service.resolve(uri, None)
        self.assertEqual(result.value, self.structure_map.value)
