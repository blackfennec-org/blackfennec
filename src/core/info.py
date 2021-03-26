class Info():
    """Abstract base class for all types (Infos)."""

    def __init__(self, parent: Info = None):
        """Create Info with parent.

        Args:
            parent (:obj:`Info`): The parent of this Info.
        """
        self._parent = parent

    @property
    def parent(self):
        """Property for parent of this info."""
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def root(self):
        """Readonly property for :obj:`Root` of this structure."""
        return self.parent.root
