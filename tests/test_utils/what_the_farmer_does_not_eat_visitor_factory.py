from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.null import Null
from src.black_fennec.structure.string import String
from src.black_fennec.util.parameterized_visitor import ParameterizedVisitor


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
