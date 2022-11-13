from blackfennec.structure.structure import Structure
from blackfennec.document_system.document import Document

class DocumentRegistry:
    def __init__(self):
        self._documents: dict[Structure, Document] = {}

    def register_document(self, document: Document):
        self._documents[document.content] = document

    def get_document(self, structure: Structure) -> Document:
        return self._documents[structure.root]
