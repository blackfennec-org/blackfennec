from blackfennec_doubles.structure.double_structure import StructureInstanceMock


class RootMock(StructureInstanceMock):
    def __init__(self, value=None, document=None):
        super().__init__(value, self, self)
        self._document = document
        self.get_document_count = 0
        self.parent = self

    def accept(self, visitor):
        return visitor.visit_root(self)

    def get_document(self):
        self.get_document_count += 1
        return self._document

    @property
    def root(self):
        return self
