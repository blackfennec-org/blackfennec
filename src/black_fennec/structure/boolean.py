from src.black_fennec.structure.structure import Structure


class Boolean(Structure):
    """Core Type Boolean, represents booleans in the domain model."""

    def __init__(self, value: bool = False):
        """Construct Boolean with value `value`.

        Args:
            value (bool, optional): The value of the `Boolean`.
                Default item is `False`
        """
        Structure.__init__(self)
        self._value = value

    @property
    def value(self) -> bool:
        """"Property for the item of `Boolean`"""
        return self._value

    @value.setter
    def value(self, value: bool):
        self._value = value

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return 'Boolean(%s)' % self._value

    def accept(self, visitor):
        return visitor.visit_boolean(self)
