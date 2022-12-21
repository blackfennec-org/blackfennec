from blackfennec_doubles.document_system.double_document import DocumentMock
from blackfennec_doubles.layers.history.double_history import HistoryMock


class DocumentTabMock:
    def __init__(self, document, history=None):
        self.document = document or DocumentMock()
        self.history = history or HistoryMock()

        self.save_document_count = 0
        self.save_document_as_count = 0

    def save_document(self):
        self.save_document_count += 1

    def save_document_as(self, uri):
        self.save_document_as_count += 1
