import unittest

from doubles.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.structure.map import Map
from src.structure.root import Root
from src.structure.template.map_template import MapTemplate


class MapTemplateTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = FactoryBaseVisitorMock()
        self.subject = Map()
        self.subject.parent = Root(self.subject)
        self.map_template = MapTemplate(self.visitor, self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.map_template = None

    def test_can_construct(self):
        pass

    def test_can_get_repr(self):
        representation: str = self.map_template.__repr__()
        self.assertTrue(representation.startswith('MapTemplate('))