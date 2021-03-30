import unittest

from src.core.boolean import BooleanViewFactory, BooleanView

class BooleanViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        BooleanViewFactory()

    def test_can_create_boolean_view(self):
        factory = BooleanViewFactory()
        view = factory.create({})
        self.assertIsInstance(view, BooleanView)
