import unittest

from doubles.interpretation.interpretation import InterpretationMock
from doubles.structure.string import StringMock
from src.type_system.core.string.string_view import StringView
from src.type_system.core.string.string_view_factory import StringViewFactory


class StringViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        StringViewFactory()

    def test_can_create_string_view(self):
        factory = StringViewFactory()
        view = factory.create(InterpretationMock(StringMock()))
        self.assertIsInstance(view, StringView)
