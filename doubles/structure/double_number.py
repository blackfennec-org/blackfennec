from doubles.structure.double_info import InfoMock


class NumberMock(InfoMock):
    def __init__(self, value=None, children=None, parent=None, root=None):
        value = 0 if value is None else value
        InfoMock.__init__(self, value, children, parent, root)

    def accept(self, visitor):
        return visitor.visit_number(self)
