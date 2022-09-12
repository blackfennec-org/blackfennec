from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.null import Null
from src.black_fennec.structure.string import String

class WhatTheFarmerDoesNotEatVisitorFactory:
    def visit_structure(self, unused_subject: Structure):
        return ParameterizedVisitor(structure=True)

    def visit_string(self, unused_subject: String):
        return ParameterizedVisitor(string=True)

    def visit_number(self, unused_subject: Number):
        return ParameterizedVisitor(number=True)

    def visit_boolean(self, unused_subject: Boolean):
        return ParameterizedVisitor(boolean=True)

    def visit_reference(self, unused_subject: Reference):
        return ParameterizedVisitor(reference=True)

    def visit_list(self, unused_subject: List):
        return ParameterizedVisitor(list=True)

    def visit_map(self, unused_unused_subject: Map):
        return ParameterizedVisitor(map=True)
    
    def visit_null(self, unused_unused_subject: Null):
        return ParameterizedVisitor(null=True)

class ParameterizedVisitor:
    def __init__(self, default=False, **kwargs):
        self.__kwargs = kwargs
        self._default = default

    def visit_structure(self, unused_subject: Structure):
        if 'structure' in self.__kwargs:
            return self.__kwargs['structure']
        return self._default

    def visit_string(self, unused_subject: String):
        if 'string' in self.__kwargs:
            return self.__kwargs['string']
        return self._default

    def visit_number(self, unused_subject: Number):
        if 'number' in self.__kwargs:
            return self.__kwargs['number']
        return self._default

    def visit_boolean(self, unused_subject: Boolean):
        if 'boolean' in self.__kwargs:
            return self.__kwargs['boolean']
        return self._default

    def visit_reference(self, unused_subject: Reference):
        if 'reference' in self.__kwargs:
            return self.__kwargs['reference']
        return self._default

    def visit_list(self, unused_subject: List):
        if 'list' in self.__kwargs:
            return self.__kwargs['list']
        return self._default

    def visit_map(self, unused_subject: Map):
        if 'map' in self.__kwargs:
            return self.__kwargs['map']
        return self._default

    def visit_null(self, unused_subjet: Null):
        if 'null' in self.__kwargs:
            return self.__kwargs['null']
        return self._default
