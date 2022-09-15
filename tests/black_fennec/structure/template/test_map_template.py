import unittest
import pytest

from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.double_string import StringMock
from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.structure.template.double_template_parser import TemplateParserMock
from doubles.black_fennec.structure.template.double_template import TemplateMock
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.encapsulation_base.base_factory_visitor import _create_generic_class
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.list import List
from src.black_fennec.structure.string import String
from src.black_fennec.structure.template.template_parser import TemplateParser
from src.black_fennec.structure.template.template_factory import TemplateFactory
from src.black_fennec.structure.template.map_template import MapTemplate
from src.black_fennec.structure.template.template import Template
from src.visualisation.base.date_time_range.date_time_range import DateTimeRange


class MapTemplateTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = TemplateParserMock()
        self.subject = Map(
            {"type": String("Map"), "required": List(), "properties": Map()}
        )
        self.map_template = MapTemplate(self.visitor, self.subject)

    def test_can_construct(self):
        pass

    def test_calculate_coverage_map_full_coverage(self):
        subject = Map(
            {
                "structure1": StringMock("Structure"),
                "structure2": StringMock("Structure"),
            }
        )
        template = TemplateFactory().create_map()
        template.add_property("structure1", TemplateMock("Structure"))
        template.add_property("structure2", TemplateMock("Structure"))

        coverage = template.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage(3, 3))

    def test_calculate_coverage_map_half_coverage(self):
        subject = Map(
            {
                "structure1": StringMock("Structure"),
                "structure2": StringMock("Structure"),
            }
        )

        template = TemplateFactory().create_map()
        template.add_property("structure1", TemplateMock("Structure"))

        coverage = template.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage(3, 2))

    def test_calculate_coverage_map_third_coverage(self):
        subject = Map(
            {
                "structure1": StringMock("Structure"),
                "structure2": StringMock("Structure"),
                "structure3": StringMock("Structure"),
            }
        )

        template = TemplateFactory().create_map()
        template.add_property("structure1", TemplateMock("Structure"))

        coverage = template.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage(4, 2))

    def test_calculate_coverage_map_incompatible(self):
        subject = Map({"structure1": StringMock("Structure")})

        template = TemplateFactory().create_map()
        template.add_property("structure1", TemplateMock("Structure"))
        template.add_property("structure2", TemplateMock("Structure"))

        coverage = template.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage(2, 0))

    def test_calculate_coverage_wrong_type(self):
        subject = StringMock()

        template = TemplateFactory().create_map()
        template.add_property("structure1", TemplateMock("Structure"))
        template.add_property("structure2", TemplateMock("Structure"))

        coverage = template.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage.NOT_COVERED)

    def test_required_properties(self):
        template = TemplateFactory().create_map()
        s1 = TemplateMock("Structure")
        template.add_property("structure1", s1)
        template.add_property("structure2", TemplateMock("Structure"), is_required=False)

        required_properties = template.required_properties
        assert len(required_properties) == 1
        assert required_properties[0].value == "structure1"

    def test_can_tell_that_child_is_required(self):
        template = TemplateFactory().create_map()
        s1 = TemplateMock("Structure")
        s2 = TemplateMock("Structure")
        template.add_property("structure1", s1)
        template.add_property("structure2", s2, is_required=False)

        assert not template.is_child_optional(s1)

    def test_can_set_required_to_false(self):
        template = TemplateFactory().create_map()
        s1 = TemplateMock("Structure")
        template.add_property("structure1", s1)
        template.set_required("structure1", False)

        assert template.is_child_optional(s1)

    def test_can_set_required_to_true(self):
        template = TemplateFactory().create_map()
        name = "structure1"
        s1 = TemplateMock("Structure")
        template.add_property(name, s1, is_required=False)
        template.set_required(name, True)

        assert not template.is_child_optional(s1)
        
    def test_cannot_set_required_for_none_property(self):
        template = TemplateFactory().create_map()
        name = "structure1"
        s1 = TemplateMock("Structure")
        with pytest.raises(AssertionError):
            template.set_required(name, True)

    def test_can_tell_that_child_is_optional(self):
        template = TemplateFactory().create_map()
        s1 = TemplateMock("Structure")
        s2 = TemplateMock("Structure")
        template.add_property("structure1", s1)
        template.add_property("structure2", s2, is_required=False)

        assert template.is_child_optional(s2)

    def test_can_set_child_optional(self):
        template = TemplateFactory().create_map()
        name = "structure1"
        s1 = TemplateMock("Structure")
        template.add_property(name, s1, is_required=False)
        template.set_is_child_optional(s1, False)

        assert not template.is_child_optional(s1)

    def test_cannot_set_none_child_optionality(self):
        template = TemplateFactory().create_map()
        name = "structure1"
        s1 = TemplateMock("Structure")
        with pytest.raises(AssertionError):
            template.set_is_child_optional(s1, True)

    def test_can_create_instance(self):
        map_structure = self.map_template.create_instance()
        self.assertIsInstance(map_structure, Map)

    def test_can_get_repr(self):
        representation: str = self.map_template.__repr__()
        self.assertTrue(representation.startswith("MapTemplate("))
