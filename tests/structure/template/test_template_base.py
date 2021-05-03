# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.double_dummy import Dummy
from doubles.structure.double_info import InfoMock
from doubles.structure.template.double_template_factory import TemplateFactoryMock
from src.structure.template.template_base import TemplateBase


class TemplateFactoryTestSuite(unittest.TestCase):
    def setUp(self):
        self.property_storage = dict()
        self.factory = TemplateFactoryMock()
        self.parent = Dummy('parent')
        self.root = Dummy('root')
        self.subject = InfoMock(parent=self.parent, root=self.root)
        self.template_base: Optional[TemplateBase] = TemplateBase(self.subject, self.factory, self.property_storage)

    def tearDown(self) -> None:
        self.property_storage = None
        self.factory = None
        self.subject = None
        self.template_base: Optional[TemplateBase] = None

    def test_can_construct(self):
        pass

    def test_subject_getter(self):
        self.assertEqual(self.template_base.subject, self.subject)

    def test_optional_getter(self):
        self.assertEqual(self.template_base.optional, False)

    def test_optional_setter(self):
        self.template_base.optional = True
        self.assertEqual(self.template_base.optional, True)

    def test_parent_getter(self):
        self.factory._create_return = self.parent
        parent = self.template_base.parent
        self.assertEqual(self.factory._subject, self.parent)
        self.assertEqual(self.factory._create_calls, 1)

    def test_parent_setter(self):
        self.factory._create_return = self.parent
        new_parent = Dummy('new_parent')
        self.template_base.parent = new_parent
        parent = self.template_base.parent
        self.assertEqual(self.factory._subject, new_parent)
        self.assertEqual(self.factory._create_calls, 1)

    def test_root_getter(self):
        self.factory._create_return = self.root
        root = self.template_base.root
        self.assertEqual(self.factory._subject, self.root)
        self.assertEqual(self.factory._create_calls, 1)
