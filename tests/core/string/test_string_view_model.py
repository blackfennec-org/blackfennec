import unittest

from doubles.core import StringMock, InterprationMock
from src.core.string import StringViewModel

class StringViewModelTestSuite(unittest.TestCase):
    def test_can_construct(self):
        StringViewModel(InterprationMock(StringMock()))

    def test_can_get_value(self):
        string_view_model = StringViewModel(InterprationMock(StringMock()))
        self.assertEqual(string_view_model.value, '')

    def test_can_set_value(self):
        string_view_model = StringViewModel(InterprationMock())
        string_view_model.value = 'Black Fennec'
        self.assertEqual(string_view_model.value, 'Black Fennec')
