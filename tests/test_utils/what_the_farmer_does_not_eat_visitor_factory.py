from blackfennec.structure.boolean import Boolean
from blackfennec.structure.structure import Structure
from blackfennec.structure.list import List
from blackfennec.structure.map import Map
from blackfennec.structure.number import Number
from blackfennec.structure.reference import Reference
from blackfennec.structure.null import Null
from blackfennec.structure.string import String
from blackfennec.util.parameterized_visitor import ParameterizedVisitor


class WhatTheFarmerDoesNotEatVisitorFactory:
    def visit_structure(self, unused_subject: Structure):
        return ParameterizedVisitor(structure=lambda s: True)

    def visit_string(self, unused_subject: String):
        return ParameterizedVisitor(string=lambda s: True)

    def visit_number(self, unused_subject: Number):
        return ParameterizedVisitor(number=lambda s: True)

    def visit_boolean(self, unused_subject: Boolean):
        return ParameterizedVisitor(boolean=lambda s: True)

    def visit_reference(self, unused_subject: Reference):
        return ParameterizedVisitor(reference=lambda s: True)

    def visit_list(self, unused_subject: List):
        return ParameterizedVisitor(list=lambda s: True)

    def visit_map(self, unused_unused_subject: Map):
        return ParameterizedVisitor(map=lambda s: True)

    def visit_null(self, unused_unused_subject: Null):
        return ParameterizedVisitor(null=True)
