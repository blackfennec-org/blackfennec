import numbers
from src.black_fennec.structure.structure import Structure


class Number(Structure):
    """Core Type Number, represents numbers in the domain model."""

    def __init__(self, value: numbers.Number = 0):
        """Construct Number with item `item`.

        Args:
            value (:obj:`numbers.Number`, optional): The item of the `Number`.
                By default "" (empty number)
        """
        Structure.__init__(self)
        self._value = value

    @property
    def value(self) -> numbers.Number:
        """"Property for the item of `Number`"""
        return self._value

    @value.setter
    def value(self, value: numbers.Number):
        self._value = value

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return 'Number(%s)' % self._value

    def accept(self, visitor):
        return visitor.visit_number(self)
