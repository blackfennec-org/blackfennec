import numbers
import unittest
from doubles.black_fennec.structure.double_root import RootMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.number import Number


class NumberTestSuite(unittest.TestCase):
    def test_can_construct(self):
        number = Number(3.141)
        self.assertAlmostEqual(number.value, 3.141)

    def test_can_default_construct(self):
        number = Number()
        self.assertAlmostEqual(number.value, 0)

    def test_can_get_value(self):
        number = Number(3.141)
        self.assertAlmostEqual(number.value, 3.141)

    def test_can_set_value(self):
        number = Number()
        number.value = 2.718
        self.assertAlmostEqual(number.value, 2.718)

    def test_can_change_parent(self):
        new_parent = RootMock()
        number = Number()
        number.parent = new_parent
        self.assertEqual(number.parent, new_parent)

    def test_representation(self):
        actual = Number(3.141)
        expected = 'Number(%s)' % actual.value
        self.assertEqual(actual.__repr__(), expected)

    def test_accept(self):
        visitor = FactoryBaseVisitorMock()
        number = Number()
        number.accept(visitor)
        self.assertEqual(visitor.number, number)
        self.assertEqual(visitor.visit_number_count, 1)
