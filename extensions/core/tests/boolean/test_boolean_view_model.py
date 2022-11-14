import unittest

from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.structure.double_boolean import BooleanMock
from core.boolean.boolean_view_model import BooleanViewModel


class BooleanViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        BooleanViewModel(InterpretationMock())

    def test_can_get_value(self):
        boolean_view_model = BooleanViewModel(InterpretationMock(BooleanMock()))
        self.assertFalse(boolean_view_model.boolean.value)

    def test_can_set_value(self):
        boolean_view_model = BooleanViewModel(InterpretationMock())
        boolean_view_model.value = True
        self.assertTrue(boolean_view_model.value)
