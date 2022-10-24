from blackfennec.structure.structure import Structure
from blackfennec.structure.list import List
from blackfennec.structure.map import Map
from blackfennec.structure.null import Null
from blackfennec.structure.reference import Reference
from blackfennec.structure.string import String
from blackfennec.structure.number import Number
from blackfennec.structure.boolean import Boolean
from blackfennec.structure.visitor import Visitor


class InterceptingVisitor(Visitor):
    def __init__(self, adapter, visitor):
        self.adapter = adapter
        self.visitor = visitor

    def visit_structure(self, subject: Structure):
        return self.visitor.visit_structure(self.adapter(subject))

    def visit_string(self, subject: String):
        return self.visitor.visit_string(self.adapter(subject))

    def visit_number(self, subject: Number):
        return self.visitor.visit_number(self.adapter(subject))

    def visit_boolean(self, subject: Boolean):
        return self.visitor.visit_boolean(self.adapter(subject))

    def visit_reference(self, subject: Reference):
        return self.visitor.visit_reference(self.adapter(subject))

    def visit_null(self, subject: Null):
        return self.visitor.visit_null(self.adapter(subject))

    def visit_list(self, subject: List):
        return self.visitor.visit_list(self.adapter(subject))

    def visit_map(self, subject: Map):
        return self.visitor.visit_map(self.adapter(subject))
