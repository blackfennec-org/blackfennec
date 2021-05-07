# -*- coding: utf-8 -*-
from src.structure.encapsulation_base.map_encapsulation_base import MapEncapsulationBase
from src.structure.map import Map
from src.structure.overlay.overlay_base import OverlayBase


class MapOverlay(MapEncapsulationBase, OverlayBase):
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
