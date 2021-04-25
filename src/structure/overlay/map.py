# -*- coding: utf-8 -*-
from src.structure.map import Map


class MapToOverlayAdapter(Map):
    def __init__(self, adaptee: Map):
        super().__init__()
        self._adaptee = adaptee

    @property
    def adaptee(self) -> Map:
        return self._adaptee

    @property
    def parent(self) -> 'MapToOverlayAdapter':
        """Property for parent of this info."""
        return MapToOverlayAdapter(self.adaptee.parent)

    @property
    def children(self) -> ['MapToOverlayAdapter']:
        """Property for children of this info.
        Returns:
            [MapToOverlayAdapter]: Empty list
        """
        return list()

    @property
    def root(self) -> 'MapToOverlayAdapter':
        return MapToOverlayAdapter(self.adaptee.root)