from doubles.black_fennec.structure.double_info import InfoMock


class RootMock(InfoMock):
    def __init__(self, value=None, children=None):
        InfoMock.__init__(self, value, children, self, self)

    def accept(self, visitor):
        return visitor.visit_root(self)

