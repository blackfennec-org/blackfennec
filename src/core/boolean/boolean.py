from src.core.info import Info

class Boolean(Info):
    """Core Type Boolean, represents booleans in the domain model."""

    def __init__(self, value: bool = False):
        """Construct Boolean with value `value`.

        Args:
            value (:obj:`bool`, optional): The value of the `Boolean`.
                Default value is `False`
        """
        Info.__init__(self)
        self._value = value

    @property
    def value(self) -> bool:
        """"Property for the value of `Boolean`"""
        return self._value

    @value.setter
    def value(self, value: bool):
        self._value = value

    def __eq__(self, other) -> bool:
        return self._value == bool(other)

    def __ne__(self, other) -> bool:
        return not self == other

    def __bool__(self) -> bool:
        """Truth value of Boolean"""
        return self._value

    def __str__(self) -> str:
        """Convert to string"""
        return str(self._value)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return 'Boolean(%s)' % self._value
