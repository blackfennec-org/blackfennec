# -*- coding: utf-8 -*-
from src.structure.string import String


class StringToOverlayAdapter(String):
    def __init__(self, adaptee: String):
        super().__init__()
        self._adaptee = adaptee

    @property
    def adaptee(self) -> String:
        return self._adaptee

    @property
    def parent(self) -> 'StringToOverlayAdapter':
        """Property for parent of this info."""
        return StringToOverlayAdapter(self.adaptee.parent)

    @property
    def children(self) -> ['StringToOverlayAdapter']:
        return list()

    @property
    def root(self) -> 'StringToOverlayAdapter':
        return StringToOverlayAdapter(self.adaptee.root)