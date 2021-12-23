import unittest
from tests.black_fennec.structure.test_structure import StructureTestMixin
from doubles.black_fennec.structure.double_root import RootMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.string import String


class StringTestSuite(StructureTestMixin, unittest.TestCase):
    def setUp(self):
        self.structure_type_name = 'String'
        self.default_value = 'Black Fennec'
        self.alternative_value = 'Tiny Fennec'
    
    def create_structure(self, value):
        return String(value)

    def test_can_construct(self):
        string = String('Black Fennec')
        self.assertEqual(string.value, 'Black Fennec')

    def test_can_default_construct(self):
        number = String()
        self.assertAlmostEqual(number.value, '')
