from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.null import Null
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.string import String
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.visitor import Visitor

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