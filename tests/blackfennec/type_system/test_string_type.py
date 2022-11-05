import unittest

from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.structure.double_number import NumberMock
from blackfennec_doubles.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from blackfennec.interpretation.auction.coverage import Coverage
from blackfennec.structure.string import String
from blackfennec.structure.map import Map
from blackfennec.type_system.string_type import StringType
from blackfennec.type_system.type import Type


class StringTypeTestSuite(unittest.TestCase):
    def setUp(self):
        self.subject = String()
        self.string_type = StringType(self.subject)

    def test_can_construct(self):
        pass

    def test_can_calculate_coverage(self):
        coverage = self.string_type.calculate_coverage(self.subject)
        self.assertEqual(coverage, Coverage.COVERED)

    def test_can_cover_string(self):
        subject = String("Black Fennec")
        coverage = self.string_type.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage.COVERED)

    def test_can_calculate_coverage_pattern_match(self):
        type = Map({"pattern": String("[a-z]")})
        string_type = StringType(type)
        subject = String("a")
        coverage = string_type.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage.COVERED)

    def test_can_calculate_coverage_normal_string(self):
        type = Map({"pattern": String("Test")})
        string_type = StringType(type)
        subject = String("Test123")
        coverage = string_type.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage.COVERED)

    def test_can_calculate_coverage_pattern_mismatch(self):
        type = Map({"pattern": String("[a-z]")})
        string_type = StringType(type)
        subject = String("A")
        coverage = string_type.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage.NOT_COVERED)

    def test_calculate_coverage_wrong_type(self):
        subject = NumberMock()

        coverage = self.string_type.calculate_coverage(subject)
        self.assertEqual(coverage, Coverage.NOT_COVERED)

    def test_can_create_instance(self):
        string_structure = self.string_type.create_instance()
        self.assertIsInstance(string_structure, String)

    def test_can_get_repr(self):
        representation: str = self.string_type.__repr__()
        self.assertTrue(representation.startswith("StringType("))
