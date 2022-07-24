import numbers
import unittest
from tests.black_fennec.structure.test_structure import StructureTestMixin
from doubles.black_fennec.structure.double_root import RootMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.number import Number


class NumberTestSuite(StructureTestMixin, unittest.TestCase):

    def setUp(self):
        self.structure_type_name = "Number"
        self.default_value = 3.141
        self.alternative_value = 2.718

    def create_instance(self, value):
        return Number(value)

    def test_can_construct(self):
        number = Number(3.141)
        self.assertAlmostEqual(number.value, 3.141)

    def test_can_default_construct(self):
        number = Number()
        self.assertAlmostEqual(number.value, 0)
