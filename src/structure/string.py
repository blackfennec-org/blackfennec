from collections import UserString
from src.structure.info import Info


class String(Info, UserString):
    """Core Type String, represents strings in the domain model."""

    def __init__(self, value: str = ""):
        """Construct String with value `value`.

        Args:
            value (:obj:`str`, optional): The value of the `String`.
                By default "" (empty string)
        """
        Info.__init__(self)
        UserString.__init__(self, value)

    @property
    def value(self):
        """"Property for the value of `String`"""
        return self.data

    @value.setter
    def value(self, value: str):
        self.data = value
