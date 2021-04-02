import unittest

from src.core.number import NumberViewFactory, NumberView

class NumberViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        NumberViewFactory()

    def test_can_create_number_view(self):
        factory = NumberViewFactory()
        view = factory.create({})
        self.assertIsInstance(view, NumberView)
