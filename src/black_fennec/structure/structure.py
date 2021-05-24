# -*- coding: utf-8 -*-


class Structure:
    """Abstract base class for all types (Structures)."""

    def __init__(self, value=None, parent: 'Structure' = None):
        """Create Structure with parent.

        Args:
            parent (:obj:`Structure`): The parent of this Structure.
        """
        self._parent: 'Structure' = parent
        self._value = value

    @property
    def value(self):
        """Property for value contained in this structure"""
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def parent(self) -> 'Structure':
        """Property for parent of this structure."""
        return self._parent

    @parent.setter
    def parent(self, parent: 'Structure'):
        self._parent = parent

    @property
    def children(self) -> list:
        """Readonly property for children of this Structure, by default empty."""
        return list()

    @property
    def root(self) -> 'Root':
        """Readonly property for :obj:`Root` of this structure."""
        return self.parent.root

    def accept(self, visitor):
        return visitor.visit_structure(self)

    def __hash__(self):
        return hash(id(self))
