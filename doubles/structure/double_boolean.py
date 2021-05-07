from doubles.structure.double_info import InfoMock


class BooleanMock(InfoMock):
    def __init__(self, value=None, children=None, parent=None, root=None):
        InfoMock.__init__(self, value, children, parent, root)

    def accept(self, visitor):
        return visitor.visit_number(self)
