import unittest

from uri import URI
from doubles.double_dummy import Dummy
from doubles.black_fennec.structure.double_info import InfoMock
from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.structure.double_list import ListMock
from doubles.black_fennec.structure.double_reference import ReferenceMock
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.info import Info
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.root import Root
from src.black_fennec.structure.string import String
from src.black_fennec.structure.visitors.deep_copy_visitor import \
    DeepCopyVisitor


class TestDeepCopyVisitorTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = DeepCopyVisitor()

    def test_visit_info(self):
        with self.assertRaises(NotImplementedError):
            self.visitor.visit_info(Dummy('info'))

    def test_visit_root(self):
        with self.assertRaises(NotImplementedError):
            self.visitor.visit_root(Dummy('root'))

    def test_visit_string(self):
        info = InfoMock(value='string_value')
        copy = self.visitor.visit_string(info)
        self.assertEqual(info.value, copy.value)
        

    def test_visit_number(self):
        info = InfoMock(value=1337)
        copy = self.visitor.visit_number(info)
        self.assertEqual(info.value, copy.value)

    def test_visit_boolean(self):
        info = InfoMock(value=True)
        copy = self.visitor.visit_boolean(info)
        self.assertEqual(info.value, copy.value)

    def test_visit_reference(self):
        info = ReferenceMock(value=URI('ref'))
        copy = self.visitor.visit_reference(info)
        self.assertEqual(info.value, copy.value)

    def test_visit_list(self):
        info = ListMock(value=[ListMock(value=[])])
        copy = self.visitor.visit_list(info)
        self.assertEqual(info.value, copy.value)

    def test_visit_map(self):
        info = MapMock(value={'key': MapMock(value={})})
        copy = self.visitor.visit_map(info)
        self.assertEqual(info.value, copy.value)
