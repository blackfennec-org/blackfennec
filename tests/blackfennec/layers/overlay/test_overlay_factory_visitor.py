# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from blackfennec_doubles.structure.double_structure import StructureInstanceMock
from blackfennec.layers.overlay.overlay_base import OverlayBase
from blackfennec.layers.overlay.overlay_factory_visitor import OverlayFactoryVisitor

from blackfennec.structure.map import Map
from blackfennec.structure.reference import Reference
from blackfennec.structure.string import String

from blackfennec.structure.reference_navigation.parent_navigator import ParentNavigator
from blackfennec.structure.reference_navigation.child_navigator import ChildNavigator

class OverlayFactoryVisitorTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = OverlayFactoryVisitor()

    def test_can_construct(self):
        pass

    def test_can_visit_structure(self):
        structure = StructureInstanceMock()
        structure_overlay = self.visitor.visit_structure(structure)
        self.assertIsInstance(structure_overlay, OverlayBase)

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

    def test_can_resolve_double_reference(self):
        map = Map({
            "a": Reference([ ParentNavigator(), ChildNavigator("b"), ChildNavigator("c") ]),
            "b": Map({
                "c": Reference([ ParentNavigator(), ChildNavigator("d") ]),
                "d": String("value"),
            })
        })
        overlay = map.accept(self.visitor)

        assert overlay.value["a"].value == "value"
