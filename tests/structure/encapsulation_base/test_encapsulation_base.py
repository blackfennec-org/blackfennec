# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.double_dummy import Dummy
from doubles.structure.double_info import InfoMock
from doubles.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.structure.encapsulation_base.encapsulation_base import EncapsulationBase


class EncapsulationBaseTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = FactoryBaseVisitorMock()
        self.parent = InfoMock()
        self.root = InfoMock()
        self.subject = InfoMock(parent=self.parent, root=self.root)
        self.encapsulation_base: Optional[EncapsulationBase] = EncapsulationBase(self.visitor, self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.encapsulation_base: Optional[EncapsulationBase] = None
    
    def test_subject_getter(self):
        self.assertEqual(self.encapsulation_base.subject, self.subject)

    def test_parent_getter(self):
        parent = self.encapsulation_base.parent
        self.assertEqual(self.visitor.info, self.parent)
        self.assertEqual(self.visitor.visit_info_count, 1)

    def test_parent_setter(self):
        new_parent = InfoMock('new_parent')
        self.encapsulation_base.parent = new_parent
        parent = self.encapsulation_base.parent
        self.assertEqual(self.visitor.info, new_parent)
        self.assertEqual(self.visitor.visit_info_count, 1)

    def test_root_getter(self):
        self.encapsulation_base.root
        self.assertEqual(self.visitor.info, self.root)
        self.assertEqual(self.visitor.visit_info_count, 1)

    def test_can_get_repr(self):
        representation: str = self.encapsulation_base.__repr__()
        self.assertTrue(representation.startswith('EncapsulationBase('))
