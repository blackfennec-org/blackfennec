from blackfennec_doubles.structure.double_structure import StructureMock


class StringMock(StructureMock):
    def __init__(self, value=None, parent=None, root=None):
        value = '' if value is None else value
        StructureMock.__init__(self, value, parent, root)
        self.type_name = 'String'

    def accept(self, visitor):
        return visitor.visit_string(self)

    def __eq__(self, other):
        return (self.value, self.parent) == (other.value, other.parent)

    def __str__(self):
        return self._value
