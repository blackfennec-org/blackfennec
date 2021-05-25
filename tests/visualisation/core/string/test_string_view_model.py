import unittest

from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.structure.double_string import StringMock
from src.visualisation.core.string.string_view_model import StringViewModel


class StringViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        StringViewModel(InterpretationMock(StringMock()))

    def test_can_get_value(self):
        string_view_model = StringViewModel(InterpretationMock(StringMock()))
        self.assertEqual(string_view_model.value, '')

    def test_can_set_value(self):
        string_view_model = StringViewModel(InterpretationMock())
        string_view_model.value = 'Black Fennec'
        self.assertEqual(string_view_model.value, 'Black Fennec')