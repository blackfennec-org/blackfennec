# -*- coding: utf-8 -*-
from src.structure.number import Number


class NumberToOverlayAdapter(Number):
    def __init__(self, adaptee: Number):
        super().__init__()
        self._adaptee = adaptee

    @property
    def adaptee(self) -> Number:
        return self._adaptee

    @property
    def parent(self) -> 'NumberToOverlayAdapter':
        """Property for parent of this info."""
        return NumberToOverlayAdapter(self.adaptee.parent)

    @property
    def children(self) -> ['NumberToOverlayAdapter']:
        """Property for children of this info.
        Returns:
            [NumberToOverlayAdapter]: Empty list
        """
        return list()

    @property
    def root(self) -> 'NumberToOverlayAdapter':
        return NumberToOverlayAdapter(self.adaptee.root)