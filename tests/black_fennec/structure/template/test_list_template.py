import unittest

from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.template.double_template import TemplateMock
from doubles.black_fennec.structure.double_string import StringMock
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.list import List
from src.black_fennec.structure.string import String
from src.black_fennec.structure.template.list_template import ListTemplate
from src.black_fennec.structure.template.template_parser import TemplateParser
from src.black_fennec.structure.template.template_factory import TemplateFactory


class ListTemplateTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = TemplateParser()
        self.subject = Map({"elements": List()})
        self.list_template = ListTemplate(self.visitor, self.subject)

    def test_can_construct(self):
        pass

    def test_coverage_getter_list_full_coverage(self):
        subject = List([StringMock("Structure1"), StringMock("Structure2")])

        template = TemplateFactory().create_list()
        template.add_element(TemplateMock("Structure"))

        coverage = template.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage(3, 3))

    def test_coverage_getter_list_half_coverage(self):
        subject = List([StringMock("Structure1"), List([StringMock("List Item 1")])])

        template = TemplateFactory().create_list()
        template.add_element(TemplateMock("Structure"))

        coverage = template.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage(3, 2))

    def test_calculate_coverage_wrong_type(self):
        subject = StringMock()

        coverage = self.list_template.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage.NOT_COVERED)

    def test_can_create_instance(self):
        list_structure = self.list_template.create_instance()
        self.assertIsInstance(list_structure, List)

    def test_can_get_repr(self):
        representation: str = self.list_template.__repr__()
        self.assertTrue(representation.startswith("ListTemplate("))
