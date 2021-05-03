# -*- coding: utf-8 -*-
from src.structure.list import List
from src.structure.overlay.overlay_factory import OverlayFactory
from src.structure.overlay.overlay_base import OverlayBase
from src.structure.reference import Reference


class ListOverlay(OverlayBase, List):
    def __init__(self, subject: List, overlay_factory):
        List.__init__(self)
        OverlayBase.__init__(self, subject, overlay_factory)

    @property
    def subject(self) -> List:
        return self._subject

    @property
    def children(self) -> [OverlayBase]:
        """Property for children of this info.
        Returns:
            [ListTemplate]: Empty list
        """
        result: list = list()
        for child in super().children:
            result.append(child)
            if isinstance(child, Reference):
                reference: Reference = child
                result.append(reference.destination)
        return result

    def __getitem__(self, index):
        item = super().__getitem__(index)
        return self._overlay_factory.create(item)

    def __setitem__(self, index, value):
        decapsulated_value = value
        if isinstance(value, OverlayBase):
            subject: OverlayBase = value
            decapsulated_value = subject.subject
        List.__setitem__(self, index, decapsulated_value)