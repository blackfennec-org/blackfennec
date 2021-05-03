# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.double_dummy import Dummy
from doubles.structure.double_info import InfoMock
from doubles.structure.filter.double_filter_factory import FilterFactoryMock
from src.structure.filter.filter_base import FilterBase


class FilterFactoryTestSuite(unittest.TestCase):
    def setUp(self):
        self.property_storage = dict()
        self.factory = FilterFactoryMock()
        self.parent = Dummy('parent')
        self.root = Dummy('root')
        self.subject = InfoMock(parent=self.parent, root=self.root)
        self.filter_base: Optional[FilterBase] = FilterBase(self.subject, self.factory, self.property_storage)

    def tearDown(self) -> None:
        self.property_storage = None
        self.factory = None
        self.subject = None
        self.filter_base: Optional[FilterBase] = None

    def test_can_construct(self):
        pass

    def test_subject_getter(self):
        self.assertEqual(self.filter_base.subject, self.subject)

    def test_filter_getter(self):
        self.assertEqual(self.filter_base.filter, False)

    def test_filter_setter(self):
        self.filter_base.filter = True
        self.assertEqual(self.filter_base.filter, True)

    def test_parent_getter(self):
        self.factory._create_return = self.parent
        parent = self.filter_base.parent
        self.assertEqual(self.factory._subject, self.parent)
        self.assertEqual(self.factory._create_calls, 1)

    def test_parent_setter(self):
        self.factory._create_return = self.parent
        new_parent = Dummy('new_parent')
        self.filter_base.parent = new_parent
        parent = self.filter_base.parent
        self.assertEqual(self.factory._subject, new_parent)
        self.assertEqual(self.factory._create_calls, 1)

    def test_root_getter(self):
        self.factory._create_return = self.root
        root = self.filter_base.root
        self.assertEqual(self.factory._subject, self.root)
        self.assertEqual(self.factory._create_calls, 1)
