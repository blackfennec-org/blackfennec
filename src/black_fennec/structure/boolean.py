from src.black_fennec.structure.info import Info


class Boolean(Info):
    """Core Type Boolean, represents booleans in the domain model."""

    def __init__(self, value: bool = False):
        """Construct Boolean with item `item`.

        Args:
            value (:obj:`bool`, optional): The item of the `Boolean`.
                Default item is `False`
        """
        Info.__init__(self)
        self._value = value

    @property
    def value(self) -> bool:
        """"Property for the item of `Boolean`"""
        return self._value

    @value.setter
    def value(self, value: bool):
        self._value = value

    def __eq__(self, other) -> bool:
        return self._value == bool(other)

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self):
        return hash(id(self))

    def __bool__(self) -> bool:
        """Truth item of Boolean"""
        return self._value

    def __str__(self) -> str:
        """Convert to string"""
        return str(self._value)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return 'Boolean(%s)' % self._value

    def accept(self, visitor):
        return visitor.visit_boolean(self)
