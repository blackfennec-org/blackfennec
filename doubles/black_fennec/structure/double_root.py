from doubles.black_fennec.structure.double_structure import StructureMock


class RootMock(StructureMock):
    def __init__(self, value=None, children=None):
        StructureMock.__init__(self, value, children, self, self)

    def accept(self, visitor):
        return visitor.visit_root(self)

