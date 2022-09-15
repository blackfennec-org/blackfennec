import unittest
import pytest

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

    def test_can_add_element(self):
        template = TemplateFactory().create_list()
        s1 = TemplateMock("Structure")
        template.add_element(s1)

        assert len(template.elements) == 1

    def test_can_add_required_element(self):
        template = TemplateFactory().create_list()
        s1 = TemplateMock("Structure")
        template.add_element(s1)

        assert len(template.required_elements) == 1

    def test_can_add_optional_element(self):
        template = TemplateFactory().create_list()
        s1 = TemplateMock("Structure")
        template.add_element(s1, is_required=False)

        assert len(template.required_elements) == 0

    def test_can_make_index_required(self):
        template = TemplateFactory().create_list()
        s1 = TemplateMock("Structure")
        template.add_element(s1)
        template.set_required(0, False)

        assert len(template.required_elements) == 0


    def test_can_make_index_optional(self):
        template = TemplateFactory().create_list()
        s1 = TemplateMock("Structure")
        template.add_element(s1, is_required=False)
        template.set_required(0, True)

        assert len(template.required_elements) == 1

    def test_can_tell_that_child_is_optional(self):
        template = TemplateFactory().create_list()
        s1 = TemplateMock("Structure")
        s2 = TemplateMock("Structure")
        template.add_element(s1)
        template.add_element(s2, is_required=False)

        assert template.is_child_optional(s2)

    def test_can_tell_that_child_is_required(self):
        template = TemplateFactory().create_list()
        s1 = TemplateMock("Structure")
        s2 = TemplateMock("Structure")
        template.add_element(s1)
        template.add_element(s2, is_required=True)

        assert not template.is_child_optional(s2)

    def test_can_set_child_optional(self):
        template = TemplateFactory().create_list()
        s1 = TemplateMock("Structure")
        template.add_element(s1, is_required=True)
        template.set_is_child_optional(s1, False)

        assert not template.is_child_optional(s1)

    def test_cannot_set_none_child_optionality(self):
        template = TemplateFactory().create_list()
        name = "structure1"
        s1 = TemplateMock("Structure")
        with pytest.raises(AssertionError):
            template.set_is_child_optional(s1, True)

    def test_can_create_instance(self):
        list_structure = self.list_template.create_instance()
        self.assertIsInstance(list_structure, List)

    def test_can_get_repr(self):
        representation: str = self.list_template.__repr__()
        self.assertTrue(representation.startswith("ListTemplate("))
