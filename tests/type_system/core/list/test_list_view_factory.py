import unittest

from doubles.interpretation.interpretation import InterpretationMock
from doubles.structure.list import ListMock
from src.type_system.core.list.list_view import ListView
from src.type_system.core.list.list_view_factory import ListViewFactory


class MapViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ListViewFactory()

    def test_can_create_list_view(self):
        factory = ListViewFactory()
        view = factory.create(InterpretationMock(ListMock()))
        self.assertIsInstance(view, ListView)
