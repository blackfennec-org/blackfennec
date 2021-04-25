# -*- coding: utf-8 -*-
from src.structure.list import List
from src.structure.reference import Reference


class ListToOverlayAdapter(List):
    def __init__(self, adaptee: List):
        super().__init__()
        self._adaptee = adaptee

    @property
    def adaptee(self) -> List:
        return self._adaptee

    @property
    def parent(self) -> 'ListToOverlayAdapter':
        """Property for parent of this info."""
        return ListToOverlayAdapter(self.adaptee.parent)

    @property
    def children(self) -> ['ListToOverlayAdapter']:
        """Property for children of this info.
        Returns:
            [ListToOverlayAdapter]: Empty list
        """
        result: list = list()
        for child in super().children:
            result.append(child)
            if isinstance(child, Reference):
                reference: Reference = child
                result.append(reference.destination)


    @property
    def root(self) -> 'ListToOverlayAdapter':
        return ListToOverlayAdapter(self.adaptee.root)