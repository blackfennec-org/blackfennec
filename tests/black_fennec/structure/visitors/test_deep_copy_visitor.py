import unittest

from src.black_fennec.util.deep_compare.deep_compare import DeepCompare
from doubles.black_fennec.structure.double_list import ListMock
from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.structure.double_reference import ReferenceMock
from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.double_dummy import Dummy
from src.black_fennec.structure.visitors.deep_copy_visitor import \
    DeepCopyVisitor
from uri import URI


class TestDeepCopyVisitorTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = DeepCopyVisitor()

    def test_visit_structure(self):
        with self.assertRaises(NotImplementedError):
            self.visitor.visit_structure(Dummy('structure'))

    def test_visit_string(self):
        structure = StructureMock(value='string_value')
        copy = self.visitor.visit_string(structure)
        self.assertEqual(structure.value, copy.value)

    def test_visit_number(self):
        structure = StructureMock(value=1337)
        copy = self.visitor.visit_number(structure)
        self.assertEqual(structure.value, copy.value)

    def test_visit_boolean(self):
        structure = StructureMock(value=True)
        copy = self.visitor.visit_boolean(structure)
        self.assertEqual(structure.value, copy.value)

    def test_visit_reference(self):
        structure = ReferenceMock(value=URI('ref'))
        copy = self.visitor.visit_reference(structure)
        self.assertEqual(structure.value, copy.value)

    def test_visit_list(self):
        structure = ListMock(value=[ListMock(value=[])])
        copy = self.visitor.visit_list(structure)
        self.assertTrue(DeepCompare.compare(structure, copy))

    def test_visit_map(self):
        structure = MapMock(value={'key': MapMock(value={})})
        copy = self.visitor.visit_map(structure)
        self.assertTrue(DeepCompare.compare(structure, copy))
