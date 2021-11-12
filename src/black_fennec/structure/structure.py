# -*- coding: utf-8 -*-


class Structure:
    """Abstract base class for all types (Structures)."""

    def __init__(self, parent: 'Structure' = None):
        """Create Structure with parent.

        Args:
            parent (Structure): The parent of this Structure.
        """
        self._parent: 'Structure' = parent

    @property
    def parent(self) -> 'Structure':
        """Property for parent of this structure."""
        return self._parent

    @parent.setter
    def parent(self, parent: 'Structure'):
        self._parent = parent

    @property
    def root(self) -> 'Root':
        """Readonly property for `Root` of this structure."""
        return self.parent.root

    def accept(self, visitor):
        return visitor.visit_structure(self)

    def __hash__(self):
        """Hash function required for any structure
            to act as a key in a dictionary"""
        return hash(id(self))
