from blackfennec.structure.boolean import Boolean
from blackfennec.structure.structure import Structure
from blackfennec.structure.list import List
from blackfennec.structure.map import Map
from blackfennec.structure.number import Number
from blackfennec.structure.reference import Reference
from blackfennec.structure.null import Null
from blackfennec.structure.string import String
from blackfennec.structure.visitor import Visitor


class ParameterizedVisitor(Visitor):
    def __init__(self, default=lambda s: False, **kwargs):
        self.__kwargs = kwargs
        self._default = default

    def _return(self, key, subject):
        if key in self.__kwargs:
            arg = self.__kwargs[key]
            if callable(arg):
                return arg(subject)
            return arg
        return self._default(subject)

    def visit_structure(self, subject: Structure):
        return self._return("structure", subject)

    def visit_list(self, subject: List):
        return self._return("list", subject)

    def visit_map(self, subject: Map):
        return self._return("map", subject)

    def visit_reference(self, subject: Reference):
        return self._return("reference", subject)

    def visit_null(self, subject: Null):
        return self._return("null", subject)

    def visit_string(self, subject: String):
        return self._return("string", subject)

    def visit_number(self, subject: Number):
        return self._return("number", subject)

    def visit_boolean(self, subject: Boolean):
        return self._return("boolean", subject)
