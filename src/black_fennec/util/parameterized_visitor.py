from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.string import String


class ParameterizedVisitor:
    def __init__(self, default=lambda s: False, **kwargs):
        self.__kwargs = kwargs
        self._default = default

    def visit_structure(self, subject: Structure):
        if "structure" in self.__kwargs:
            return self.__kwargs["structure"](subject)
        return self._default(subject)

    def visit_string(self, subject: String):
        if "string" in self.__kwargs:
            return self.__kwargs["string"](subject)
        return self._default(subject)

    def visit_number(self, subject: Number):
        if "number" in self.__kwargs:
            return self.__kwargs["number"](subject)
        return self._default(subject)

    def visit_boolean(self, subject: Boolean):
        if "boolean" in self.__kwargs:
            return self.__kwargs["boolean"](subject)
        return self._default(subject)

    def visit_reference(self, subject: Reference):
        if "reference" in self.__kwargs:
            return self.__kwargs["reference"](subject)
        return self._default(subject)

    def visit_list(self, subject: List):
        if "list" in self.__kwargs:
            return self.__kwargs["list"](subject)
        return self._default(subject)

    def visit_map(self, subject: Map):
        if "map" in self.__kwargs:
            return self.__kwargs["map"](subject)
        return self._default(subject)
