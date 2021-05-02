import unittest

from doubles.double_dummy import Dummy
from doubles.structure.double_list import ListMock
from doubles.util.json.double_json_reference_resolving_service import JsonReferenceResolvingServiceMock
from src.structure.reference import Reference


class ReferenceTestSuite(unittest.TestCase):
    def test_can_construct(self):
        reference = Reference(Dummy(), 'ref')

    def test_get_reference(self):
        reference_str = 'ref'
        reference = Reference(Dummy(), reference_str)
        self.assertEqual(reference.reference, reference_str)

    def test_set_reference(self):
        reference_str = 'ref'
        reference = Reference(Dummy())
        reference.reference = reference_str
        self.assertEqual(reference.reference, reference_str)

    def test_get_destination(self):
        reference_str = 'ref'
        reference_resolving_service = JsonReferenceResolvingServiceMock(resolve_return=reference_str)
        reference = Reference(reference_resolving_service, reference_str)
        destination = reference.destination
        self.assertEqual(destination, reference_str)
        self.assertEqual(reference_resolving_service.resolve_count, 1)
        self.assertEqual(reference_resolving_service.reference, reference_str)
        self.assertEqual(reference_resolving_service.source, reference)

    def test_get_children_no_destination(self):
        reference_str = 'ref'
        reference_resolving_service = JsonReferenceResolvingServiceMock(resolve_return=None)
        reference = Reference(reference_resolving_service, reference_str)
        self.assertEqual(len(reference.children), 0)

    def test_get_children_with_destination_set(self):
        reference_str = 'ref'
        children = [0,1]
        info = ListMock(children=children)
        reference_resolving_service = JsonReferenceResolvingServiceMock(resolve_return=info)
        reference = Reference(reference_resolving_service, reference_str)
        self.assertEqual(children, reference.children)

    def test_is_json_reference(self):
        reference = dict()
        reference[Reference.REFERENCE_KEY] = 'ref'
        self.assertTrue(Reference.is_json_reference(reference))

    def test_is_json_reference_with_no_json_reference(self):
        reference = dict()
        reference[Reference.REFERENCE_KEY + '$'] = 'ref'
        self.assertFalse(Reference.is_json_reference(reference))

    def test_equal_equal_elements(self):
        comp = Reference(Dummy(), 'ref')
        equal_comp = Reference(Dummy(), 'ref')
        self.assertTrue(
            comp == equal_comp,
            msg='Equal elements are not equal'
        )

    def test_equal_unequal_elements(self):
        comp = Reference(Dummy(), 'ref1')
        other_comp = Reference(Dummy(), 'ref2')
        self.assertFalse(
            comp == other_comp,
            msg='Unequal elements are equal'
        )

    def test_not_equal_equal_elements(self):
        comp = Reference(Dummy(), 'ref')
        equal_comp = Reference(Dummy(), 'ref')
        self.assertFalse(
            comp != equal_comp,
            msg='Equal elements are not equal'
        )

    def test_not_equal_unequal_elements(self):
        comp = Reference(Dummy(), 'ref1')
        other_comp = Reference(Dummy(), 'ref2')
        self.assertTrue(
            comp != other_comp,
            msg='Unequal elements are equal'
        )

    def test_to_string(self):
        reference_str = 'ref'
        reference = Reference(Dummy(), reference_str)
        expected = reference_str
        self.assertEqual(str(reference), expected)

    def test_representation(self):
        reference_str = 'ref'
        reference = Reference(Dummy(), reference_str)
        expected = 'Reference(ref)'
        self.assertEqual(repr(reference), expected)
