import unittest

from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.structure.double_number import NumberMock
from src.visualisation.core.number.number_view_model import NumberViewModel


class NumberViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        NumberViewModel(InterpretationMock(NumberMock()))

    def test_can_get_value(self):
        number_view_model = NumberViewModel(InterpretationMock(NumberMock()))
        self.assertEqual(number_view_model.value, 0)

    def test_can_set_value(self):
        number_view_model = NumberViewModel(InterpretationMock())
        number_view_model.value = 3.141
        self.assertEqual(number_view_model.value, 3.141)
