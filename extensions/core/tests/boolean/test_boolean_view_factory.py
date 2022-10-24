import unittest
from blackfennec_doubles.interpretation.double_interpretation import InterpretationMock
from blackfennec_doubles.structure.double_boolean import BooleanMock
from blackfennec.interpretation.specification import Specification
from core.boolean.boolean_preview import BooleanPreview
from core.boolean.boolean_view import BooleanView
from core.boolean.boolean_view_factory import BooleanViewFactory


class BooleanViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        BooleanViewFactory()

    def test_can_create_boolean_view(self):
        factory = BooleanViewFactory()
        view = factory.create(
            InterpretationMock(BooleanMock()))
        self.assertIsInstance(view, BooleanView)

    def test_can_create_boolean_preview(self):
        factory = BooleanViewFactory()
        interpretation = InterpretationMock(
            BooleanMock(), 
            specification=Specification(request_preview=True))
        view = factory.create(interpretation)
        self.assertIsInstance(view, BooleanPreview)

    def test_satisfies_default(self):
        factory = BooleanViewFactory()
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_satisfy_preview(self):
        factory = BooleanViewFactory()
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertTrue(satisfies)
