# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.black_fennec.structure.double_structure import StructureInstanceMock
from doubles.black_fennec.structure.double_list import ListInstanceMock
from doubles.black_fennec.structure.double_map import MapInstanceMock
from src.black_fennec.structure.overlay.overlay_factory_visitor import OverlayFactoryVisitor
from src.black_fennec.structure.overlay.list_overlay import ListOverlay
from src.black_fennec.structure.overlay.map_overlay import MapOverlay
from src.black_fennec.structure.overlay.overlay_base import OverlayBase


class OverlayFactoryVisitorTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor: Optional[OverlayFactoryVisitor] = OverlayFactoryVisitor()

    def tearDown(self) -> None:
        self.visitor: Optional[OverlayFactoryVisitor] = None

    def test_can_construct(self):
        pass

    def test_can_visit_structure(self):
        structure = StructureInstanceMock()
        structure_overlay = self.visitor.visit_structure(structure)
        self.assertIsInstance(structure_overlay, OverlayBase)

    def test_can_visit_list(self):
        structure_list = ListInstanceMock()
        list_overlay = self.visitor.visit_list(structure_list)
        self.assertIsInstance(list_overlay, ListOverlay)

    def test_can_visit_map(self):
        structure_map = MapInstanceMock()
        map_overlay = self.visitor.visit_map(structure_map)
        self.assertIsInstance(map_overlay, MapOverlay)

    def test_visit_caches_class(self):
        structure = StructureInstanceMock()
        structure_overlay_type = type(self.visitor.visit_structure(structure))
        self.assertIsInstance(self.visitor.visit_structure(structure), structure_overlay_type)

    def test_generic_overlay_subject(self):
        structure = StructureInstanceMock()
        structure_overlay = self.visitor.visit_structure(structure).subject
        # checking a property type is not possible thus,
        # only the existence is checked:
        # https://stackoverflow.com/questions/52201094/check-underlying-type-of-a-property-in-python
        self.assertIsNotNone(structure_overlay)
