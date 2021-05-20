# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.black_fennec.structure.double_info import InfoInstanceMock
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

    def test_can_visit_info(self):
        info = InfoInstanceMock()
        info_template = self.visitor.visit_info(info)
        self.assertIsInstance(info_template, TemplateBase)

    def test_can_visit_list(self):
        info_list = ListInstanceMock()
        list_template = self.visitor.visit_list(info_list)
        self.assertIsInstance(list_template, ListTemplate)

    def test_can_visit_map(self):
        info_map = MapInstanceMock()
        map_template = self.visitor.visit_map(info_map)
        self.assertIsInstance(map_template, MapTemplate)

    def test_visit_caches_class(self):
        info = InfoInstanceMock()
        info_template_type = type(self.visitor.visit_info(info))
        self.assertIsInstance(self.visitor.visit_info(info), info_template_type)

    def test_generic_template_subject(self):
        info = InfoInstanceMock()
        info_template = self.visitor.visit_info(info).subject
        # checking a property type is not possible thus,
        # only the existence is checked:
        # https://stackoverflow.com/questions/52201094/check-underlying-type-of-a-property-in-python
        self.assertIsNotNone(info_template)