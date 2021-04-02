import unittest

from src.core.string import StringViewFactory, StringView

class StringViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        StringViewFactory()

    def test_can_create_string_view(self):
        factory = StringViewFactory()
        view = factory.create({})
        self.assertIsInstance(view, StringView)