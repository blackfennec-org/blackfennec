# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.black_fennec.structure.double_structure import StructureInstanceMock
from doubles.black_fennec.structure.double_list import ListInstanceMock
from doubles.black_fennec.structure.double_map import MapInstanceMock
from src.black_fennec.structure.template.template_factory_visitor import TemplateFactoryVisitor
from src.black_fennec.structure.template.list_template import ListTemplate
from src.black_fennec.structure.template.map_template import MapTemplate
from src.black_fennec.structure.template.template_base import TemplateBase


class TemplateFactoryVisitorTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor: Optional[TemplateFactoryVisitor] = TemplateFactoryVisitor()

    def tearDown(self) -> None:
        self.visitor: Optional[TemplateFactoryVisitor] = None

    def test_can_construct(self):
        pass

    def test_can_get_metadata_storage(self):
        metadata = self.visitor.metadata_storage
        self.assertIsInstance(metadata, dict)

    def test_can_visit_structure(self):
        structure = StructureInstanceMock()
        structure_template = self.visitor.visit_structure(structure)
        self.assertIsInstance(structure_template, TemplateBase)

    def test_can_visit_list(self):
        structure_list = ListInstanceMock()
        list_template = self.visitor.visit_list(structure_list)
        self.assertIsInstance(list_template, ListTemplate)

    def test_can_visit_map(self):
        structure_map = MapInstanceMock()
        map_template = self.visitor.visit_map(structure_map)
        self.assertIsInstance(map_template, MapTemplate)

    def test_visit_caches_class(self):
        structure = StructureInstanceMock()
        structure_template_type = type(self.visitor.visit_structure(structure))
        self.assertIsInstance(self.visitor.visit_structure(structure), structure_template_type)

    def test_generic_template_subject(self):
        structure = StructureInstanceMock()
        structure_template = self.visitor.visit_structure(structure).subject
        # checking a property type is not possible thus,
        # only the existence is checked:
        # https://stackoverflow.com/questions/52201094/check-underlying-type-of-a-property-in-python
        self.assertIsNotNone(structure_template)
