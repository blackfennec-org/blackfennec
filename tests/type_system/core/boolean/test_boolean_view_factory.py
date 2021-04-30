import unittest
from doubles.interpretation.double_interpretation import InterpretationMock
from doubles.structure.double_boolean import BooleanMock
from src.interpretation.specification import Specification
from src.type_system.core.boolean.boolean_preview import BooleanPreview
from src.type_system.core.boolean.boolean_view import BooleanView
from src.type_system.core.boolean.boolean_view_factory import BooleanViewFactory


class BooleanViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        BooleanViewFactory()

    def test_can_create_boolean_view(self):
        factory = BooleanViewFactory()
        specification = Specification()
        view = factory.create(
            InterpretationMock(BooleanMock()), specification)
        self.assertIsInstance(view, BooleanView)

    def test_can_create_boolean_preview(self):
        factory = BooleanViewFactory()
        specification = Specification(request_preview=True)
        view = factory.create(InterpretationMock(BooleanMock()), specification)
        self.assertIsInstance(view, BooleanPreview)

    def test_satisfies_default(self):
        factory = BooleanViewFactory()
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_satisfy_preview(self):
        factory = BooleanViewFactory()
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertTrue(satisfies)
