class DocumentTabMock:
    def __init__(self, document):
        self.document = document
        self.save_document_count = 0
        self.save_document_as_count = 0

    def save_document(self):
        self.save_document_count += 1

    def save_document_as(self, uri):
        self.save_document_as_count += 1
