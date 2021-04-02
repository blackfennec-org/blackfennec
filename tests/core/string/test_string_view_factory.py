import unittest

from doubles.core.interpretation import InterprationMock
from doubles.core.string import StringMock
from src.core.string import StringViewFactory, StringView

class StringViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        StringViewFactory()

    def test_can_create_string_view(self):
        factory = StringViewFactory()
        view = factory.create(InterprationMock(StringMock()))
        self.assertIsInstance(view, StringView)
