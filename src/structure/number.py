import numbers
from src.structure.info import Info


class Number(Info):
    """Core Type Number, represents numbers in the domain model."""

    def __init__(self, value: numbers.Number = 0):
        """Construct Number with item `item`.

        Args:
            value (:obj:`numbers.Number`, optional): The item of the `Number`.
                By default "" (empty number)
        """
        Info.__init__(self)
        self._value = value

    @property
    def value(self) -> numbers.Number:
        """"Property for the item of `Number`"""
        return self._value

    @value.setter
    def value(self, value: numbers.Number):
        self._value = value

    def __add__(self, value) -> 'Number':
        """Add two numbers together"""
        if isinstance(value, Number):
            value = value.value
        return Number(self._value + value)

    def __iadd__(self, value) -> 'Number':
        """Add a number to this number"""
        if isinstance(value, Number):
            value = value.value
        self._value += value
        return self

    def __eq__(self, other) -> bool:
        """Test for equality"""
        if isinstance(other, Number):
            other = other.value
        return self._value == other

    def __str__(self) -> str:
        """Convert to string"""
        return str(self._value)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return 'Number(%s)' % self._value

    def accept(self, visitor):
        return visitor.visit_number(self)
