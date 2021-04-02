import unittest

from doubles.core.interpretation import InterprationMock
from doubles.core.list import ListMock
from src.core.list import ListViewFactory, ListView

class MapViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ListViewFactory()

    def test_can_create_list_view(self):
        factory = ListViewFactory()
        view = factory.create(InterprationMock(ListMock()))
        self.assertIsInstance(view, ListView)
