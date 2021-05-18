import unittest

from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.list import List
from src.black_fennec.structure.root import Root
from src.black_fennec.structure.template.list_template import ListTemplate


class ListTemplateTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = FactoryBaseVisitorMock()
        self.subject = List()
        self.subject.parent = Root(self.subject)
        self.list_template = ListTemplate(self.visitor, self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.list_template = None

    def test_can_construct(self):
        pass

    def test_can_get_repr(self):
        representation: str = self.list_template.__repr__()
        self.assertTrue(representation.startswith('ListTemplate('))