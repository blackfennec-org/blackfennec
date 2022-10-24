import unittest
from tests.blackfennec.structure.test_structure import StructureTestMixin
from blackfennec_doubles.structure.double_root import RootMock
from blackfennec_doubles.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from blackfennec.structure.string import String


class StringTestSuite(StructureTestMixin, unittest.TestCase):
    def setUp(self):
        self.structure_type_name = 'String'
        self.default_value = 'Black Fennec'
        self.alternative_value = 'Tiny Fennec'
    
    def create_instance(self, value):
        return String(value)

    def test_can_construct(self):
        string = String('Black Fennec')
        self.assertEqual(string.value, 'Black Fennec')

    def test_can_default_construct(self):
        number = String()
        self.assertAlmostEqual(number.value, '')
