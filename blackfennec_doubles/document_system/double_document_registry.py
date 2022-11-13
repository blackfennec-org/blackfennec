
class DocumentRegistryMock:
    def __init__(self):
        self.registered_document = None

    def register_document(self, document):
        self.registered_document = document

    def get_document(self, content):
        return self.registered_document
