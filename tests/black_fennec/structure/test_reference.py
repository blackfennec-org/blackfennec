import unittest
from uri import URI
from tests.black_fennec.structure.test_structure import StructureTestMixin
from doubles.double_dummy import Dummy
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from doubles.black_fennec.util.json.double_json_reference_resolving_service import JsonReferenceResolvingServiceMock
from src.black_fennec.structure.reference import Reference


class ReferenceTestSuite(StructureTestMixin, unittest.TestCase):
    def setUp(self):
        self.structure_type_name = 'Reference'
        self.default_value = URI('ref')
        self.alternative_value = URI('alt_ref')

    def create_structure(self, value):
        return Reference(Dummy(), value)

    def test_can_construct(self):
        Reference(Dummy(), URI('ref'))

    def test_get_destination(self):
        reference_uri = URI('ref')
        reference_resolving_service = JsonReferenceResolvingServiceMock(
            resolve_return=reference_uri)
        reference = Reference(reference_resolving_service, reference_uri)
        destination = reference.destination
        self.assertEqual(destination, reference_uri)
        self.assertEqual(reference_resolving_service.resolve_count, 1)
        self.assertEqual(reference_resolving_service.reference, reference_uri)
        self.assertEqual(reference_resolving_service.source, reference)
