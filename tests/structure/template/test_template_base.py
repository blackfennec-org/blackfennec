# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.double_dummy import Dummy
from doubles.structure.double_info import InfoMock
from doubles.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.structure.template.template_base import TemplateBase


class TemplateBaseTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = FactoryBaseVisitorMock()
        self.parent = InfoMock()
        self.root = InfoMock()
        self.subject = InfoMock(parent=self.parent, root=self.root)
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

    def test_can_get_repr(self):
        representation: str = self.template_base.__repr__()
        self.assertTrue(representation.startswith('TemplateBase('))