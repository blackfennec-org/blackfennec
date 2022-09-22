from src.black_fennec.structure.map import Map
from src.black_fennec.structure.type.boolean_type import BooleanType
from src.black_fennec.structure.type.type_parser import TypeParser


class BooleanTemplate(BooleanType):
    """Template of boolean.

    Class creates Template structure for core type
        boolean."""

    def __init__(self):
        BooleanType.__init__(self, Map())

        self._name = "Boolean"

    @property
    def name(self):
        return self._name
