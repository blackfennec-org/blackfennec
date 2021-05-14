from collections import UserString
from src.structure.info import Info


class String(Info, UserString):
    """Core Type String, represents strings in the domain model."""

    def __init__(self, value: str = ""):
        """Construct String with item `item`.

        Args:
            value (:obj:`str`, optional): The item of the `String`.
                By default "" (empty string)
        """
        Info.__init__(self)
        UserString.__init__(self, value)

    @property
    def value(self):
        """"Property for the item of `String`"""
        return self.data

    @value.setter
    def value(self, value: str):
        self.data = value

    def accept(self, visitor):
        return visitor.visit_string(self)
