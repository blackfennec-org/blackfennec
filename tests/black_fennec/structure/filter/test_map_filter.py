import unittest

from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.root import Root
from src.black_fennec.structure.filter.map_filter import MapFilter


class MapFilterTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = FactoryBaseVisitorMock()
        self.subject = Map()
        self.subject.parent = Root(self.subject)
        self.map_filter = MapFilter(self.visitor, self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.map_filter = None

    def test_can_construct(self):
        pass

    def test_can_get_repr(self):
        representation: str = self.map_filter.__repr__()
        self.assertTrue(representation.startswith('MapFilter('))