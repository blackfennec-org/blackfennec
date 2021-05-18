# -*- coding: utf-8 -*-
from src.black_fennec.structure.encapsulation_base.map_encapsulation_base import MapEncapsulationBase
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.overlay.overlay_base import OverlayBase


class MapOverlay(MapEncapsulationBase, OverlayBase):
    """Base Class for Overlay of a Map."""
    def __init__(
            self,
            visitor: 'TemplateFactoryVisitor',
            subject: Map,
    ):
        MapEncapsulationBase.__init__(
            self,
            visitor,
            subject
        )
        OverlayBase.__init__(
            self,
            visitor,
            subject
        )

    def __getitem__(self, key):
        item = self.subject[key]
        return self._encapsulate_and_dereference(item)

    def __repr__(self):
        return f'MapOverlay({self.subject.__repr__()})'
