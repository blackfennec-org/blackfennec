from blackfennec_doubles.structure.double_structure import StructureMock


class NumberMock(StructureMock):
    def __init__(self, value=None, parent=None, root=None):
        value = 0 if value is None else value
        StructureMock.__init__(self, value, parent, root)
        self.type_name = 'Number'

    def accept(self, visitor):
        return visitor.visit_number(self)
