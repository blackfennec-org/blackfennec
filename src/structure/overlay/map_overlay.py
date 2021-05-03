# -*- coding: utf-8 -*-
from src.structure.map import Map
from src.structure.overlay.overlay_base import OverlayBase
from src.structure.reference import Reference


class MapOverlay(OverlayBase, Map):
    def __init__(self, subject: Map, overlay_factory):
        OverlayBase.__init__(self, subject, overlay_factory)

    @property
    def subject(self) -> Map:
        return self._subject

    @property
    def children(self) -> [OverlayBase]:
        """Property for children of this info.
        Returns:
            [MapTemplate]: Empty list
        """
        result: list = list()
        for child in self.subject.children:
            if isinstance(child, Reference):
                reference: Reference = child
                result.append(
                    self._overlay_factory.create(
                        reference.destination
                    )
                )
            else:
                result.append(self._overlay_factory.create(child))
        return result

    def __getitem__(self, key):
        item = self.subject[key]
        return self._overlay_factory.create(item)

    def __setitem__(self, key, value):
        self.subject[key] = self._remove_overlay_class(value)

    def __repr__(self):
        return f'MapOverlay({self.subject.__repr__()})'
