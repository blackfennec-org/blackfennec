import unittest

from uri import URI

from doubles.double_dummy import Dummy
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from doubles.black_fennec.util.json.double_json_reference_resolving_service import JsonReferenceResolvingServiceMock
from src.black_fennec.structure.reference import Reference


class ReferenceTestSuite(unittest.TestCase):
    def test_can_construct(self):
        Reference(Dummy(), URI('ref'))

    def test_get_value(self):
        reference_uri = URI('ref')
        reference = Reference(Dummy(), reference_uri)
        self.assertEqual(reference.value, reference_uri)

    def test_set_value(self):
        reference_uri = URI('ref')
        reference = Reference(Dummy())
        reference.value = reference_uri
        self.assertEqual(reference.value, reference_uri)

    def test_get_destination(self):
        reference_uri = URI('ref')
        reference_resolving_service = JsonReferenceResolvingServiceMock(resolve_return=reference_uri)
        reference = Reference(reference_resolving_service, reference_uri)
        destination = reference.destination
        self.assertEqual(destination, reference_uri)
        self.assertEqual(reference_resolving_service.resolve_count, 1)
        self.assertEqual(reference_resolving_service.reference, reference_uri)
        self.assertEqual(reference_resolving_service.source, reference)

    def test_get_children_no_destination(self):
        reference_uri = URI('ref')
        reference_resolving_service = JsonReferenceResolvingServiceMock(resolve_return=None)
        reference = Reference(reference_resolving_service, reference_uri)
        self.assertEqual(len(reference.children), 0)

    def test_to_string(self):
        reference_uri = URI('ref')
        reference = Reference(Dummy(), reference_uri)
        expected = reference_uri
        self.assertEqual(str(reference), expected)

    def test_representation(self):
        reference_uri = URI('ref')
        reference = Reference(Dummy(), reference_uri)
        expected = 'Reference(ref)'
        self.assertEqual(repr(reference), expected)

    def test_accept(self):
        visitor = FactoryBaseVisitorMock()
        reference = Reference(Dummy())
        reference.accept(visitor)
        self.assertEqual(visitor.reference, reference)
        self.assertEqual(visitor.visit_reference_count, 1)
