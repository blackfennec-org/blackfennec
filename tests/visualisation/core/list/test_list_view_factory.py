import unittest

from doubles.black_fennec.interpretation.double_interpretation import InterpretationMock
from doubles.black_fennec.interpretation.double_interpretation_service import InterpretationServiceMock
from doubles.black_fennec.structure.double_list import ListMock
from src.black_fennec.interpretation.specification import Specification
from src.visualisation.core.list.list_preview import ListPreview
from src.visualisation.core.list.list_view import ListView
from src.visualisation.core.list.list_view_factory import ListViewFactory


class MapViewFactoryTestSuite(unittest.TestCase):
    def test_can_construct(self):
        ListViewFactory(InterpretationServiceMock([]))

    def test_can_create_list_view(self):
        factory = ListViewFactory(InterpretationServiceMock([]))
        view = factory.create(
            InterpretationMock(ListMock()),
            Specification())
        self.assertIsInstance(view, ListView)

    def test_can_create_list_preview(self):
        factory = ListViewFactory(InterpretationServiceMock([]))
        view = factory.create(InterpretationMock(
            ListMock()), Specification(request_preview=True))
        self.assertIsInstance(view, ListPreview)

    def test_satisfies_default(self):
        factory = ListViewFactory(InterpretationServiceMock([]))
        satisfies = factory.satisfies(Specification())
        self.assertTrue(satisfies)

    def test_does_satisfy_preview(self):
        factory = ListViewFactory(InterpretationServiceMock([]))
        satisfies = factory.satisfies(Specification(request_preview=True))
        self.assertTrue(satisfies)
