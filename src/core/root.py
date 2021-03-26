from src.core.info import Info

class Root(Info):
    """Info that is the Root of a structure."""
    def __init__(self):
        super().__init__(self)

    @property
    def parent(self):
        """Readonly property for parent of Root.

        The inherited setter for this property has been overridden
            to disallow chanching the parent of the root.
            If the operation is attempted a TypeError is raised.
        """
        return super().parent

    @parent.setter
    def parent(self, new_parent):
        raise TypeError("cannot set parent on type Root")

    @property
    def root(self):
        """Readonly property for root of structure; returns self."""
        return self
