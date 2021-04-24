import unittest

from doubles.interpretation.double_interpretation import InterpretationMock
from doubles.structure.double_number import NumberMock
from src.interpretation.specification import Specification
from src.type_system.core.number.number_view import NumberView
from src.type_system.core.number.number_view_factory import NumberViewFactory


class NumberViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        NumberViewFactory()

    def test_can_create_number_view(self):
        factory = NumberViewFactory()
        view = factory.create(
            InterpretationMock(NumberMock()),
            Specification())
        self.assertIsInstance(view, NumberView)

    def test_satisfies_default(self):
        factory = NumberViewFactory()
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_not_satisfy_preview(self):
        factory = NumberViewFactory()
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertFalse(satisfies)
