# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.black_fennec.structure.double_structure import StructureMock, StructureInstanceMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.template.template_base import TemplateBase


class TemplateBaseTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = FactoryBaseVisitorMock()
        self.parent = StructureMock()
        self.subject = StructureMock(parent=self.parent)
        self.template_base: Optional[TemplateBase] = TemplateBase(self.visitor, self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.template_base: Optional[TemplateBase] = None

    def test_can_construct(self):
        pass

    def test_optional_getter(self):
        self.assertEqual(self.template_base.optional, False)

    def test_optional_setter(self):
        self.template_base.optional = True
        self.assertEqual(self.template_base.optional, True)

    def test_can_calculate_coverage_of_structure(self):
        structure = StructureInstanceMock('Structure')
        coverage = self.template_base.calculate_coverage(structure)
        self.assertEqual(coverage, Coverage.COVERED)

    def test_can_visit_structure(self):
        structure = StructureInstanceMock('Structure')
        coverage = structure.accept(self.template_base)
        self.assertEqual(coverage, Coverage.COVERED)

    def test_has_create_structure_interface(self):
        func = self.template_base.create_structure
        self.assertIsNotNone(func)

    def test_can_get_repr(self):
        representation: str = self.template_base.__repr__()
        self.assertTrue(representation.startswith('TemplateBase('))
