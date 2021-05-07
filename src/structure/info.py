# -*- coding: utf-8 -*-


class Info:
    """Abstract base class for all types (Infos)."""

    def __init__(self, value=None, parent: 'Info' = None):
        """Create Info with parent.

        Args:
            parent (:obj:`Info`): The parent of this Info.
        """
        self._parent: 'Info' = parent
        self._value = value

    @property
    def value(self):
        """Property for value contained in this info"""
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def parent(self) -> 'Info':
        """Property for parent of this info."""
        return self._parent

    @parent.setter
    def parent(self, parent: 'Info'):
        self._parent = parent

    @property
    def children(self) -> list:
        """Readonly property for children of this Info, by default empty."""
        return list()

    @property
    def root(self) -> 'Root':
        """Readonly property for :obj:`Root` of this structure."""
        return self.parent.root

    def accept(self, visitor):
        return visitor.visit_info(self)
