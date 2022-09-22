from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.black_fennec.structure.type.string_type import StringType
from src.black_fennec.structure.type.type_parser import TypeParser


class StringTemplate(StringType):
    """Template of string.

    Class creates Template structure for core type
        string."""

    def __init__(self):
        StringType.__init__(self)
        self._name = 'String'

    @property
    def name(self):
        return self._name
