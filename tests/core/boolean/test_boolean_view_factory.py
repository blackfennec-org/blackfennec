import unittest
from doubles.core.interpretation import InterprationMock
from doubles.core.boolean import BooleanMock
from src.core.boolean import BooleanViewFactory, BooleanView

class BooleanViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        BooleanViewFactory()

    def test_can_create_boolean_view(self):
        factory = BooleanViewFactory()
        view = factory.create(InterprationMock(BooleanMock()))
        self.assertIsInstance(view, BooleanView)
