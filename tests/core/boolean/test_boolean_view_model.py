import unittest

from doubles.core import BooleanMock, InterprationMock
from src.core.boolean import BooleanViewModel

class BooleanViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        BooleanViewModel(InterprationMock())

    def test_can_get_value(self):
        boolean_view_model = BooleanViewModel(InterprationMock(BooleanMock()))
        self.assertFalse(boolean_view_model.value)

    def test_can_set_value(self):
        boolean_view_model = BooleanViewModel(InterprationMock())
        boolean_view_model.value = True
        self.assertTrue(boolean_view_model.value)
