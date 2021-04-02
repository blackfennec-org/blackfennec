import unittest

from doubles.core.interpretation import InterprationMock
from doubles.core.number import NumberMock
from src.core.number import NumberViewFactory, NumberView

class NumberViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        NumberViewFactory()

    def test_can_create_number_view(self):
        factory = NumberViewFactory()
        view = factory.create(InterprationMock(NumberMock()))
        self.assertIsInstance(view, NumberView)
