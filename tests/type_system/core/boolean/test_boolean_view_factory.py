import unittest
from doubles.interpretation.interpretation import InterpretationMock
from doubles.structure.boolean import BooleanMock
from src.type_system.core.boolean.boolean_view import BooleanView
from src.type_system.core.boolean.boolean_view_factory import BooleanViewFactory


class BooleanViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        BooleanViewFactory()

    def test_can_create_boolean_view(self):
        factory = BooleanViewFactory()
        view = factory.create(InterpretationMock(BooleanMock()))
        self.assertIsInstance(view, BooleanView)
