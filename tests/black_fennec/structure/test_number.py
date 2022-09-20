import numbers
import unittest
import pytest
from tests.black_fennec.structure.test_structure import StructureTestMixin
from doubles.black_fennec.structure.double_root import RootMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.map import Map


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

    def test_can_remove_equal_numbers_from_map(self):
        structure = Map()
        a = Number(1337)
        b = Number(1337)
        structure.add_item("A", a)
        structure.add_item("B", b)

        structure.remove_item("A")

    def test_can_find_number_in_list(self):
        l = [Number(1337)]
        target = Number(1337)
        for n in l:
            if n == target:
                found = n

        assert found is not None

    def test_can_check_if_number_in_list(self):
        l = [Number(1337)]
        target = Number(1337)
        assert target in l
