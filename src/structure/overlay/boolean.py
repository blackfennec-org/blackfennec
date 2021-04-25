# -*- coding: utf-8 -*-
from src.structure.boolean import Boolean


class BooleanToOverlayAdapter(Boolean):
    def __init__(self, adaptee: Boolean):
        super().__init__()
        self._adaptee = adaptee

    @property
    def adaptee(self) -> Boolean:
        return self._adaptee

    @property
    def parent(self) -> 'BooleanToOverlayAdapter':
        """Property for parent of this info."""
        return BooleanToOverlayAdapter(self.adaptee.parent)

    @property
    def children(self) -> ['BooleanToOverlayAdapter']:
        """Property for children of this info.
        Returns:
            [BooleanToOverlayAdapter]: Empty list
        """
        return list()

    @property
    def root(self) -> 'BooleanToOverlayAdapter':
        return BooleanToOverlayAdapter(self.adaptee.root)