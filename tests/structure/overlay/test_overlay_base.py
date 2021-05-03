# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.double_dummy import Dummy
from doubles.structure.double_info import InfoMock
from doubles.structure.overlay.double_overlay_factory import OverlayFactoryMock
from src.structure.overlay.overlay_base import OverlayBase


class OverlayFactoryTestSuite(unittest.TestCase):
    def setUp(self):
        self.property_storage = dict()
        self.factory = OverlayFactoryMock()
        self.parent = Dummy('parent')
        self.root = Dummy('root')
        self.subject = InfoMock(parent=self.parent, root=self.root)
        self.overlay_base: Optional[OverlayBase] = OverlayBase(self.subject, self.factory)

    def tearDown(self) -> None:
        self.property_storage = None
        self.factory = None
        self.subject = None
        self.overlay_base: Optional[OverlayBase] = None

    def test_can_construct(self):
        pass

    def test_subject_getter(self):
        self.assertEqual(self.overlay_base.subject, self.subject)

    def test_parent_getter(self):
        self.factory._create_return = self.parent
        parent = self.overlay_base.parent
        self.assertEqual(self.factory._subject, self.parent)
        self.assertEqual(self.factory._create_calls, 1)

    def test_parent_setter(self):
        self.factory._create_return = self.parent
        new_parent = Dummy('new_parent')
        self.overlay_base.parent = new_parent
        parent = self.overlay_base.parent
        self.assertEqual(self.factory._subject, new_parent)
        self.assertEqual(self.factory._create_calls, 1)

    def test_root_getter(self):
        self.factory._create_return = self.root
        root = self.overlay_base.root
        self.assertEqual(self.factory._subject, self.root)
        self.assertEqual(self.factory._create_calls, 1)
