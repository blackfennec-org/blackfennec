import unittest
from doubles.core.interpretation import InterpretationMock
from doubles.core.boolean import BooleanMock
from src.core.types.boolean import BooleanViewFactory, BooleanView


class BooleanViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        BooleanViewFactory()

    def test_can_create_boolean_view(self):
        factory = BooleanViewFactory()
        view = factory.create(InterpretationMock(BooleanMock()))
        self.assertIsInstance(view, BooleanView)
