from doubles.black_fennec.structure.double_structure import StructureMock


class RootMock(StructureMock):
    def __init__(self, value=None, document=None):
        StructureMock.__init__(self, value, self, self)
        self._document = document
        self.get_document_count = 0

    def accept(self, visitor):
        return visitor.visit_root(self)

    def get_document(self):
        self.get_document_count += 1
        return self._document
