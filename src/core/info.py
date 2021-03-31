class Info():
    """Abstract base class for all types (Infos)."""

    def __init__(self, parent:'Info'=None):
        """Create Info with parent.

        Args:
            parent (:obj:`Info`): The parent of this Info.
        """
        self._parent: 'Info' = parent

    @property
    def parent(self) -> 'Info':
        """Property for parent of this info."""
        return self._parent

    @parent.setter
    def parent(self, parent: 'Info'):
        self._parent = parent

    @property
    def children(self):
        """Readonly property for children of this Info, by default empty"""
        return list()

    @property
    def root(self) -> 'Info':
        """Readonly property for :obj:`Root` of this structure."""
        return self.parent.root
