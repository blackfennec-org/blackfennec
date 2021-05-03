# -*- coding: utf-8 -*-
from src.structure.map import Map
from src.structure.overlay.overlay_base import OverlayBase
from src.structure.reference import Reference


class MapOverlay(OverlayBase, Map):
    def __init__(self, subject: Map, overlay_factory):
        Map.__init__(self)
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
        for child in super().children:
            result.append(child)
            if isinstance(child, Reference):
                reference: Reference = child
                result.append(reference.destination)
        return result

    def __getitem__(self, key):
        item = super().__getitem__(key)
        return self._overlay_factory.create(item)

    def __setitem__(self, key, value):
        decapsulated_value = value
        if isinstance(value, OverlayBase):
            subject: OverlayBase = value
            decapsulated_value = subject.subject
        Map.__setitem__(self, key, decapsulated_value)
