import unittest

from doubles.core.interpretation import InterpretationMock
from doubles.core.types.number import NumberMock
from src.core.types.number import NumberViewFactory, NumberView


class NumberViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        NumberViewFactory()

    def test_can_create_number_view(self):
        factory = NumberViewFactory()
        view = factory.create(InterpretationMock(NumberMock()))
        self.assertIsInstance(view, NumberView)
