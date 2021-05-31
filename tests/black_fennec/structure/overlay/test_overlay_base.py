# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from uri import URI

from doubles.double_dummy import Dummy
from doubles.black_fennec.structure.double_structure import StructureMock
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
        self.subject = StructureMock(parent=self.parent, root=self.root)
        self.overlay_base: Optional[OverlayBase] = OverlayBase(self.visitor, self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.overlay_base: Optional[OverlayBase] = None

    def test_can_construct(self):
        self.assertIsNotNone(self.overlay_base)

    def test_can_get_repr(self):
        representation: str = self.overlay_base.__repr__()
        self.assertTrue(representation.startswith('OverlayBase('))