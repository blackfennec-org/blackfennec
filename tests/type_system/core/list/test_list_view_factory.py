import unittest

from doubles.interpretation.double_interpretation import InterpretationMock
from doubles.structure.double_list import ListMock
from src.interpretation.specification import Specification
from src.type_system.core.list.list_view import ListView
from src.type_system.core.list.list_view_factory import ListViewFactory


class MapViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ListViewFactory()

    def test_can_create_list_view(self):
        factory = ListViewFactory()
        view = factory.create(
            InterpretationMock(ListMock()),
            Specification())
        self.assertIsInstance(view, ListView)

    def test_satisfies_default(self):
        factory = ListViewFactory()
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_not_satisfy_preview(self):
        factory = ListViewFactory()
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertFalse(satisfies)
