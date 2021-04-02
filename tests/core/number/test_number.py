import unittest
from doubles.core import RootMock
from src.core.number import Number

class NumberTestSuite(unittest.TestCase):
    def test_can_construct(self):
        number = Number(3.141)
        self.assertAlmostEqual(number, 3.141)

    def test_can_default_construct(self):
        number = Number()
        self.assertAlmostEqual(number, 0)

    def test_can_get_value(self):
        number = Number(3.141)
        self.assertAlmostEqual(number.value, 3.141)

    def test_can_set_value(self):
        number = Number()
        number.value = 2.718
        self.assertAlmostEqual(number, 2.718)

    def test_can_change_parent(self):
        new_parent = RootMock()
        number = Number()
        number.parent = new_parent
        self.assertEqual(number.parent, new_parent)

    def test_can_get_root(self):
        root = RootMock()
        number = Number()
        number.parent = root
        self.assertEqual(number.root, root)

    def test_can_add(self):
        number = Number(3.141)
        result = number + Number(2.718)
        self.assertAlmostEqual(result, 3.141 + 2.718)

    def test_returns_core_type_number_on_add(self):
        number = Number(3.141)
        result = number + Number(2.718)
        self.assertIsInstance(result, Number)

    def test_can_add_float(self):
        number = Number(3.141)
        result = number + 2.718
        self.assertAlmostEqual(result, 3.141 + 2.718)

    def test_can_increment(self):
        number = Number(3.141)
        number += Number(2.718)
        self.assertAlmostEqual(number, 3.141 + 2.718)

    def test_return_core_type_number_on_increment(self):
        number = Number(3.141)
        number += Number(2.718)
        self.assertIsInstance(number, Number)

    def test_can_test_equality(self):
        self.assertEqual(Number(3.141), Number(3.141))

    def test_can_test_equality_to_float(self):
        self.assertEqual(Number(3.141), 3.141)

    def test_can_convert_to_string(self):
        self.assertEqual(str(Number(3.141)), '3.141')

    def test_representation(self):
        actual = Number(3.141)
        expected = 'Number(%s)' % actual.value
        self.assertEqual(actual.__repr__(), expected)
