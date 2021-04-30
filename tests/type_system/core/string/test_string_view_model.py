import unittest

from doubles.interpretation.double_interpretation import InterpretationMock
from doubles.structure.double_string import StringMock
from src.type_system.core.string.string_view_model import StringViewModel


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
