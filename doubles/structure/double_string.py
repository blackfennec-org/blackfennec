from doubles.structure.double_info import InfoMock


class StringMock(InfoMock):
    def __init__(self, value=None, children=None, parent=None, root=None):
        value = '' if value is None else value
        InfoMock.__init__(self, value, children, parent, root)

    def accept(self, visitor):
        return visitor.visit_string(self)

    def __eq__(self, other):
        return (self.value, self.parent) == (other.value, other.parent)

    def __str__(self):
        return self._value
