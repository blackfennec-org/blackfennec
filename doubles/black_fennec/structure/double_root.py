from doubles.black_fennec.structure.double_structure import StructureMock


class RootMock(StructureMock):
    def __init__(self, value=None):
        StructureMock.__init__(self, value, self, self)

    def accept(self, visitor):
        return visitor.visit_root(self)

