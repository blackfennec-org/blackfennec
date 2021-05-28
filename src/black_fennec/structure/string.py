from src.black_fennec.structure.structure import Structure


class String(Structure):
    """Core Type String, represents strings in the domain model."""

    def __init__(self, value: str = ''):
        """Construct String with item `item`.

        Args:
            value (:obj:`str`, optional): The item of the `String`.
                By default "" (empty string)
        """
        Structure.__init__(self)
        self.value = value

    @property
    def value(self):
        """"Property for the item of `String`"""
        return self._value

    @value.setter
    def value(self, value: str):
        self._value = value

    def accept(self, visitor):
        return visitor.visit_string(self)
