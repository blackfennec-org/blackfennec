import unittest

from doubles.interpretation.interpretation import InterpretationMock
from doubles.structure.number import NumberMock
from src.type_system.core.number.number_view import NumberView
from src.type_system.core.number.number_view_factory import NumberViewFactory


class NumberViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        NumberViewFactory()

    def test_can_create_number_view(self):
        factory = NumberViewFactory()
        view = factory.create(InterpretationMock(NumberMock()))
        self.assertIsInstance(view, NumberView)
