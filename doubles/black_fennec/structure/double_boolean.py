from doubles.black_fennec.structure.double_structure import StructureMock


class BooleanMock(StructureMock):
    def __init__(self, value=None, parent=None, root=None):
        StructureMock.__init__(self, value, parent, root)
        self.type_name = 'Boolean'

    def accept(self, visitor):
        return visitor.visit_boolean(self)
