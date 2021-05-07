# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.structure.double_info import InfoInstanceMock, InfoMock
from doubles.structure.double_list import ListInstanceMock
from doubles.structure.double_map import MapInstanceMock
from src.structure.overlay.overlay_factory_visitor import OverlayFactoryVisitor
from src.structure.overlay.list_overlay import ListOverlay
from src.structure.overlay.map_overlay import MapOverlay
from src.structure.overlay.overlay_base import OverlayBase


class OverlayFactoryVisitorTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor: Optional[OverlayFactoryVisitor] = OverlayFactoryVisitor()

    def tearDown(self) -> None:
        self.visitor: Optional[OverlayFactoryVisitor] = None

    def test_can_construct(self):
        pass

    def test_can_visit_info(self):
        info = InfoInstanceMock()
        info_overlay = self.visitor.visit_info(info)
        self.assertIsInstance(info_overlay, OverlayBase)

    def test_can_visit_list(self):
        info_list = ListInstanceMock()
        list_overlay = self.visitor.visit_list(info_list)
        self.assertIsInstance(list_overlay, ListOverlay)

    def test_can_visit_map(self):
        info_map = MapInstanceMock()
        map_overlay = self.visitor.visit_map(info_map)
        self.assertIsInstance(map_overlay, MapOverlay)

    def test_visit_caches_class(self):
        info = InfoInstanceMock()
        info_overlay_type = type(self.visitor.visit_info(info))
        self.assertIsInstance(self.visitor.visit_info(info), info_overlay_type)

    def test_generic_overlay_subject(self):
        info = InfoInstanceMock()
        info_overlay = self.visitor.visit_info(info).subject
        # checking a property type is not possible thus,
        # only the existence is checked:
        # https://stackoverflow.com/questions/52201094/check-underlying-type-of-a-property-in-python
        self.assertIsNotNone(info_overlay)
