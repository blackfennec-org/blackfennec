# -*- coding: utf-8 -*-
import unittest
import pytest

from ddt import ddt, data, unpack
from tests.test_utils.parameterize import MOCK_CORE_TYPES
from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.type.type import Type

@ddt
class TypeTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = FactoryBaseVisitorMock()
        self.parent = StructureMock()
        self.subject = StructureMock(parent=self.parent)
        self.type_base: Type = Type(self.visitor, self.subject)

    @pytest.mark.skip(reason="currently using instance of abstract class")
    def test_can_construct(self):
        pass

    @pytest.mark.skip(reason="currently using instance of abstract class")
    def test_optional_getter(self):
        self.assertEqual(self.type_base.is_optional, False)

    @pytest.mark.skip(reason="currently using instance of abstract class")
    def test_optional_setter(self):
        self.type_base.is_optional = True
        self.assertEqual(self.type_base.is_optional, True)

    @pytest.mark.skip(reason="currently using instance of abstract class")
    @data(*MOCK_CORE_TYPES[3:])
    def test_can_calculate_coverage_of_structure(self, structure):
        coverage = self.type_base.calculate_coverage(structure)
        self.assertEqual(coverage, Coverage.COVERED)

    @pytest.mark.skip(reason="currently using instance of abstract class")
    @data(*MOCK_CORE_TYPES[3:])
    def test_can_visit_structure(self, structure):
        coverage = structure.accept(self.type_base)
        self.assertEqual(coverage, Coverage.COVERED)

    @pytest.mark.skip(reason="currently using instance of abstract class")
    def test_has_create_instance_interface(self):
        func = self.type_base.create_instance
        self.assertIsNotNone(func)
