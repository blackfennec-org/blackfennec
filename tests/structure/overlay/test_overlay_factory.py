# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.structure.double_info import InfoInstanceMock, InfoMock
from doubles.structure.double_list import ListInstanceMock
from doubles.structure.double_map import MapInstanceMock
from src.structure.overlay.list_overlay import ListOverlay
from src.structure.overlay.map_overlay import MapOverlay
from src.structure.overlay.overlay_base import OverlayBase
from src.structure.overlay.overlay_factory import OverlayFactory


class OverlayFactoryTestSuite(unittest.TestCase):
    def setUp(self):
        self.factory: Optional[OverlayFactory] = OverlayFactory()

    def tearDown(self) -> None:
        self.factory: Optional[OverlayFactory] = None

    def test_can_construct(self):
        pass

    def test_can_create(self):
        info = InfoInstanceMock()
        info_overlay = self.factory.create(info)
        self.assertIsInstance(info_overlay, OverlayBase)

    def test_can_create_list(self):
        info_list = ListInstanceMock()
        list_overlay = self.factory.create(info_list)
        self.assertIsInstance(list_overlay, ListOverlay)

    def test_can_create_map(self):
        info_map = MapInstanceMock()
        map_overlay = self.factory.create(info_map)
        self.assertIsInstance(map_overlay, MapOverlay)

    def test_create_caches_class(self):
        info = InfoInstanceMock()
        info_overlay_type = type(self.factory.create(info))
        self.assertIsInstance(self.factory.create(info), info_overlay_type)

    def test_create_with_wrong_class(self):
        info = InfoMock()
        with self.assertRaises(TypeError):
            self.factory.create(info)

    def test_generic_overlay_subject(self):
        info = InfoInstanceMock()
        info_overlay = self.factory.create(info).subject
        # checking a property type is not possible thus,
        # only the existence is checked:
        # https://stackoverflow.com/questions/52201094/check-underlying-type-of-a-property-in-python
        self.assertIsNotNone(info_overlay)
