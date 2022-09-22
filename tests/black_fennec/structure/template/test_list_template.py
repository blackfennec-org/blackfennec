import unittest
import pytest

from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.type.double_type import TypeMock
from doubles.black_fennec.structure.double_string import StringMock
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.list import List
from src.black_fennec.structure.string import String
from src.black_fennec.structure.type.list_type import ListType
from src.black_fennec.structure.type.type_parser import TypeParser
from src.black_fennec.structure.type.type_factory import TypeFactory


class ListTypeTestSuite(unittest.TestCase):
    def setUp(self):
        self.subject = Map({"elements": List()})
        self.list_type = ListType(self.subject)

    def test_can_construct(self):
        pass

    def test_coverage_getter_list_full_coverage(self):
        subject = List([StringMock("Structure1"), StringMock("Structure2")])

        type = TypeFactory().create_list()
        type.add_element(TypeMock("Structure"))

        coverage = type.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage(3, 3))

    def test_coverage_getter_list_half_coverage(self):
        subject = List([StringMock("Structure1"), List([StringMock("List Item 1")])])

        type = TypeFactory().create_list()
        type.add_element(TypeMock("Structure"))

        coverage = type.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage(3, 2))

    def test_calculate_coverage_wrong_type(self):
        subject = StringMock()

        coverage = self.list_type.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage.NOT_COVERED)

    def test_can_add_element(self):
        type = TypeFactory().create_list()
        s1 = TypeMock("Structure")
        type.add_element(s1)

        assert len(type.elements) == 1

    def test_can_add_required_element(self):
        type = TypeFactory().create_list()
        s1 = TypeMock("Structure")
        type.add_element(s1)

        assert len(type.required_elements) == 1

    def test_can_add_optional_element(self):
        type = TypeFactory().create_list()
        s1 = TypeMock("Structure")
        type.add_element(s1, is_required=False)

        assert len(type.required_elements) == 0

    def test_can_make_index_required(self):
        type = TypeFactory().create_list()
        s1 = TypeMock("Structure")
        type.add_element(s1)
        type.set_required(0, False)

        assert len(type.required_elements) == 0


    def test_can_make_index_optional(self):
        type = TypeFactory().create_list()
        s1 = TypeMock("Structure")
        type.add_element(s1, is_required=False)
        type.set_required(0, True)

        assert len(type.required_elements) == 1

    def test_can_tell_that_child_is_optional(self):
        type = TypeFactory().create_list()
        s1 = TypeMock("Structure")
        s2 = TypeMock("Structure")
        type.add_element(s1)
        type.add_element(s2, is_required=False)

        assert type.is_child_optional(s2)

    def test_can_tell_that_child_is_required(self):
        type = TypeFactory().create_list()
        s1 = TypeMock("Structure")
        s2 = TypeMock("Structure")
        type.add_element(s1)
        type.add_element(s2, is_required=True)

        assert not type.is_child_optional(s2)

    def test_can_set_child_optional(self):
        type = TypeFactory().create_list()
        s1 = TypeMock("Structure")
        type.add_element(s1, is_required=True)
        type.set_is_child_optional(s1, False)

        assert not type.is_child_optional(s1)

    def test_cannot_set_none_child_optionality(self):
        type = TypeFactory().create_list()
        name = "structure1"
        s1 = TypeMock("Structure")
        with pytest.raises(AssertionError):
            type.set_is_child_optional(s1, True)

    def test_can_create_instance(self):
        list_structure = self.list_type.create_instance()
        self.assertIsInstance(list_structure, List)

    def test_can_get_repr(self):
        representation: str = self.list_type.__repr__()
        self.assertTrue(representation.startswith("ListType("))
