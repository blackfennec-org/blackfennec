import unittest

from doubles.core import NumberMock, InterprationMock
from src.core.number import NumberViewModel

class NumberViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        NumberViewModel(InterprationMock(NumberMock()))

    def test_can_get_value(self):
        number_view_model = NumberViewModel(InterprationMock(NumberMock()))
        self.assertEqual(number_view_model.value, 0)

    def test_can_set_value(self):
        number_view_model = NumberViewModel(InterprationMock())
        number_view_model.value = 3.141
        self.assertEqual(number_view_model.value, 3.141)
