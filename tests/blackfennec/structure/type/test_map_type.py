import unittest

import pytest
from blackfennec_doubles.structure.double_string import StringMock
from blackfennec_doubles.structure.type.double_type import TypeMock
from blackfennec.interpretation.auction.coverage import Coverage
from blackfennec.structure.list import List
from blackfennec.structure.map import Map
from blackfennec.structure.string import String
from blackfennec.structure.type.map_type import MapType
from blackfennec.structure.type.type_factory import TypeFactory


class MapTypeTestSuite(unittest.TestCase):
    def setUp(self):
        self.subject = Map(
            {"type": String("Map"), "required": List(), "properties": Map()}
        )
        self.map_type = MapType(self.subject)

    def test_can_construct(self):
        pass

    def test_calculate_coverage_map_full_coverage(self):
        subject = Map(
            {
                "structure1": StringMock("Structure"),
                "structure2": StringMock("Structure"),
            }
        )
        type = TypeFactory().create_map()
        type.add_property("structure1", TypeMock("Structure"))
        type.add_property("structure2", TypeMock("Structure"))

        coverage = type.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage(3, 3))

    def test_calculate_coverage_map_half_coverage(self):
        subject = Map(
            {
                "structure1": StringMock("Structure"),
                "structure2": StringMock("Structure"),
            }
        )

        type = TypeFactory().create_map()
        type.add_property("structure1", TypeMock("Structure"))

        coverage = type.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage(3, 2))

    def test_calculate_coverage_map_third_coverage(self):
        subject = Map(
            {
                "structure1": StringMock("Structure"),
                "structure2": StringMock("Structure"),
                "structure3": StringMock("Structure"),
            }
        )

        type = TypeFactory().create_map()
        type.add_property("structure1", TypeMock("Structure"))

        coverage = type.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage(4, 2))

    def test_calculate_coverage_map_incompatible(self):
        subject = Map({"structure1": StringMock("Structure")})

        type = TypeFactory().create_map()
        type.add_property("structure1", TypeMock("Structure"))
        type.add_property("structure2", TypeMock("Structure"))

        coverage = type.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage(2, 0))

    def test_calculate_coverage_wrong_type(self):
        subject = StringMock()

        type = TypeFactory().create_map()
        type.add_property("structure1", TypeMock("Structure"))
        type.add_property("structure2", TypeMock("Structure"))

        coverage = type.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage.NOT_COVERED)

    def test_required_properties(self):
        type = TypeFactory().create_map()
        s1 = TypeMock("Structure")
        type.add_property("structure1", s1)
        type.add_property("structure2", TypeMock("Structure"), is_required=False)

        required_properties = type.required_properties
        assert len(required_properties) == 1
        assert required_properties[0].value == "structure1"

    def test_can_tell_that_child_is_required(self):
        type = TypeFactory().create_map()
        s1 = TypeMock("Structure")
        s2 = TypeMock("Structure")
        type.add_property("structure1", s1)
        type.add_property("structure2", s2, is_required=False)

        assert not type.is_child_optional(s1)

    def test_can_set_required_to_false(self):
        type = TypeFactory().create_map()
        s1 = TypeMock("Structure")
        type.add_property("structure1", s1)
        type.set_required("structure1", False)

        assert type.is_child_optional(s1)

    def test_can_set_required_to_true(self):
        type = TypeFactory().create_map()
        name = "structure1"
        s1 = TypeMock("Structure")
        type.add_property(name, s1, is_required=False)
        type.set_required(name, True)

        assert not type.is_child_optional(s1)
        
    def test_cannot_set_required_for_none_property(self):
        type = TypeFactory().create_map()
        name = "structure1"
        s1 = TypeMock("Structure")
        with pytest.raises(AssertionError):
            type.set_required(name, True)

    def test_can_tell_that_child_is_optional(self):
        type = TypeFactory().create_map()
        s1 = TypeMock("Structure")
        s2 = TypeMock("Structure")
        type.add_property("structure1", s1)
        type.add_property("structure2", s2, is_required=False)

        assert type.is_child_optional(s2)

    def test_can_set_child_optional(self):
        type = TypeFactory().create_map()
        name = "structure1"
        s1 = TypeMock("Structure")
        type.add_property(name, s1, is_required=False)
        type.set_is_child_optional(s1, False)

        assert not type.is_child_optional(s1)

    def test_cannot_set_none_child_optionality(self):
        type = TypeFactory().create_map()
        name = "structure1"
        s1 = TypeMock("Structure")
        with pytest.raises(AssertionError):
            type.set_is_child_optional(s1, True)

    def test_can_create_instance(self):
        map_structure = self.map_type.create_instance()
        self.assertIsInstance(map_structure, Map)

    def test_can_get_repr(self):
        representation: str = self.map_type.__repr__()
        self.assertTrue(representation.startswith("MapType("))

    def test_can_recognize_self(self):
        assert self.map_type == self.map_type
