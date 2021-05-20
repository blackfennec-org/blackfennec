import unittest

from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.structure.double_number import NumberMock
from src.black_fennec.interpretation.specification import Specification
from src.visualisation.core.number.number_preview import NumberPreview
from src.visualisation.core.number.number_view import NumberView
from src.visualisation.core.number.number_view_factory import NumberViewFactory


class NumberViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        NumberViewFactory()

    def test_can_create_number_view(self):
        factory = NumberViewFactory()
        specification = Specification()
        view = factory.create(
            InterpretationMock(NumberMock()),
            specification)
        self.assertIsInstance(view, NumberView)

    def test_can_create_string_preview(self):
        factory = NumberViewFactory()
        specification = Specification(request_preview=True)
        view = factory.create(InterpretationMock(NumberMock()), specification)
        self.assertIsInstance(view, NumberPreview)

    def test_satisfies_default(self):
        factory = NumberViewFactory()
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_satisfy_preview(self):
        factory = NumberViewFactory()
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertTrue(satisfies)
