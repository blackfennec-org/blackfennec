from blackfennec_doubles.structure.double_structure import StructureMock


class NullMock(StructureMock):
    def __init__(self, parent=None, root=None):
        value = None
        StructureMock.__init__(self, value, parent, root)
        self.type_name = 'Null'

    def accept(self, visitor):
        return visitor.visit_null(self)
