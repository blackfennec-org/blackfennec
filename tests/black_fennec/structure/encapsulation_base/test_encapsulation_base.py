# -*- coding: utf-8 -*-
import unittest
from ddt import ddt, data, unpack
from typing import Optional
from tests.test_utils.parameterize import MOCK_CORE_STRUCTURES
from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.encapsulation_base.encapsulation_base import EncapsulationBase


@ddt
class EncapsulationBaseTestSuite(unittest.TestCase):
    def _setUp(self, parent, root, subject):
        self.visitor = FactoryBaseVisitorMock()
        self.parent = parent
        self.root = root
        self.subject = subject
        self.subject.parent = parent
        self.subject.root = root
        self.encapsulation_base: EncapsulationBase = EncapsulationBase(self.visitor, self.subject)

    def tearDown(self):
        self.visitor = None
        self.parent = None
        self.root = None
        self.subject = None
        self.encapsulation_base = None

    @data(*zip(MOCK_CORE_STRUCTURES, MOCK_CORE_STRUCTURES, MOCK_CORE_STRUCTURES))
    def test_subject_getter(self, data):
        self._setUp(*data)
        self.assertEqual(self.encapsulation_base.subject, self.subject)

    @data(*zip(MOCK_CORE_STRUCTURES, MOCK_CORE_STRUCTURES, MOCK_CORE_STRUCTURES))
    def test_parent_getter(self, data):
        self._setUp(*data)
        self.encapsulation_base.parent
        count, subject = self.visitor.get_stats(self.subject.type_name)
        self.assertEqual(subject, self.parent)
        self.assertEqual(count, 1)

    @data(*zip(MOCK_CORE_STRUCTURES, MOCK_CORE_STRUCTURES, MOCK_CORE_STRUCTURES, MOCK_CORE_STRUCTURES))
    @unpack
    def test_parent_setter(self, parent, root, subject, new_parent):
        self._setUp(parent, root, subject)
        self.encapsulation_base.parent = new_parent

        self.assertEqual(subject.parent, new_parent)

    @data(*zip(MOCK_CORE_STRUCTURES, MOCK_CORE_STRUCTURES, MOCK_CORE_STRUCTURES))
    def test_root_getter(self, data):
        self._setUp(*data)
        self.encapsulation_base.get_root()

        count, subject = self.visitor.get_stats(self.subject.type_name)
        self.assertEqual(subject, self.root)
        self.assertEqual(count, 1)
