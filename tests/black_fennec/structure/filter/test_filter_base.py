# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.black_fennec.structure.double_info import InfoMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.structure.filter.filter_base import FilterBase


class FilterBaseTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = FactoryBaseVisitorMock()
        self.parent = InfoMock()
        self.root = InfoMock()
        self.subject = InfoMock(parent=self.parent, root=self.root)
        self.filter_base: Optional[FilterBase] = FilterBase(self.visitor, self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.filter_base: Optional[FilterBase] = None

    def test_can_construct(self):
        pass

    def test_filtered_getter(self):
        self.assertEqual(self.filter_base.filtered, False)

    def test_filtered_setter(self):
        self.filter_base.filtered = True
        self.assertEqual(self.filter_base.filtered, True)

    def test_can_get_repr(self):
        representation: str = self.filter_base.__repr__()
        self.assertTrue(representation.startswith('FilterBase('))