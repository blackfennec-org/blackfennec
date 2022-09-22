from src.black_fennec.structure.map import Map
from src.black_fennec.structure.type.number_type import NumberType
from src.black_fennec.structure.type.type_parser import TypeParser


class NumberTemplate(NumberType):
    """Template of number.

    Class creates Template structure for core type
        number."""

    def __init__(self):
        NumberType.__init__(self)

        self._name = 'Number'

    @property
    def name(self):
        return self._name
