# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from uri import URI

from doubles.double_dummy import Dummy
from doubles.black_fennec.structure.double_info import InfoMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from doubles.black_fennec.util.json.double_json_reference_resolving_service import JsonReferenceResolvingServiceMock
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.overlay.overlay_base import OverlayBase
from src.black_fennec.structure.reference import Reference


class OverlayBaseTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = FactoryBaseVisitorMock()
        self.parent = Dummy('parent')
        self.root = Dummy('root')
        self.subject = InfoMock(parent=self.parent, root=self.root)
        self.overlay_base: Optional[OverlayBase] = OverlayBase(self.visitor, self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.overlay_base: Optional[OverlayBase] = None

    def test_can_construct(self):
        pass

    def test_get_list_children(self):
        value = InfoMock('test_value')
        subject = List([value])
        overlay_base: Optional[OverlayBase] = OverlayBase(
            self.visitor,
            subject
        )
        children = overlay_base.children
        self.assertEqual(len(children), 1)
        self.assertEqual(self.visitor.info, value)
        self.assertEqual(self.visitor.visit_info_count, 1)

    def test_get_list_children_with_reference(self):
        value = InfoMock('test_value')
        resolving_service = JsonReferenceResolvingServiceMock(resolve_return=value)
        ref = Reference(resolving_service, URI('0'))
        subject = List([ref])
        overlay_base: Optional[OverlayBase] = OverlayBase(
            self.visitor,
            subject
        )
        children = overlay_base.children
        self.assertEqual(len(children), 1)
        self.assertEqual(self.visitor.info, value)
        self.assertEqual(self.visitor.visit_info_count, 1)

    def test_get_map_children(self):
        key = 'test'
        value = InfoMock('test_value')
        subject = Map({key: value})
        overlay_base: Optional[OverlayBase] = OverlayBase(
            self.visitor,
            subject
        )
        children = overlay_base.children
        self.assertEqual(len(children), 1)
        self.assertEqual(self.visitor.info, value)
        self.assertEqual(self.visitor.visit_info_count, 1)

    def test_get_map_children_with_reference(self):
        key = 'test'
        value = InfoMock('test_value')
        resolving_service = \
            JsonReferenceResolvingServiceMock(resolve_return=value)
        ref = Reference(resolving_service, URI('0'))
        subject = Map({key: ref})
        overlay_base: Optional[OverlayBase] = OverlayBase(
            self.visitor,
            subject
        )
        children = overlay_base.children
        self.assertEqual(len(children), 1)
        self.assertEqual(self.visitor.info, value)
        self.assertEqual(self.visitor.visit_info_count, 1)

    def test_get_empty_children(self):
        children = self.overlay_base.children
        self.assertEqual(len(children), 0)
        self.assertEqual(self.visitor.visit_info_count, 0)

    def test_can_get_repr(self):
        representation: str = self.overlay_base.__repr__()
        self.assertTrue(representation.startswith('OverlayBase('))