# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.structure.double_info import InfoInstanceMock, InfoMock
from doubles.structure.double_list import ListInstanceMock
from doubles.structure.double_map import MapInstanceMock
from src.structure.template.list_template import ListTemplate
from src.structure.template.map_template import MapTemplate
from src.structure.template.template_base import TemplateBase
from src.structure.template.template_factory import TemplateFactory


class TemplateFactoryTestSuite(unittest.TestCase):
    def setUp(self):
        self.factory: Optional[TemplateFactory] = TemplateFactory()

    def tearDown(self) -> None:
        self.factory: Optional[TemplateFactory] = None

    def test_can_construct(self):
        pass

    def test_can_create(self):
        info = InfoInstanceMock()
        info_template = self.factory.create(info)
        self.assertIsInstance(info_template, TemplateBase)

    def test_can_create_list(self):
        info_list = ListInstanceMock()
        list_template = self.factory.create(info_list)
        self.assertIsInstance(list_template, ListTemplate)

    def test_can_create_map(self):
        info_map = MapInstanceMock()
        map_template = self.factory.create(info_map)
        self.assertIsInstance(map_template, MapTemplate)

    def test_create_caches_class(self):
        info = InfoInstanceMock()
        info_template_type = type(self.factory.create(info))
        self.assertIsInstance(self.factory.create(info), info_template_type)

    def test_create_with_wrong_class(self):
        info = InfoMock()
        with self.assertRaises(TypeError):
            self.factory.create(info)

    def test_generic_template_subject(self):
        info = InfoInstanceMock()
        info_template = self.factory.create(info).subject
        # checking a property type is not possible thus,
        # only the existence is checked:
        # https://stackoverflow.com/questions/52201094/check-underlying-type-of-a-property-in-python
        self.assertIsNotNone(info_template)
