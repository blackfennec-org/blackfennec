class UriImportStrategyFactoryMock:
    def __init__(self, import_return = None):
        self.mime_type = None
        self.file_pointer = None
        self.create_count = 0
        self._import_return = import_return

    def create(self, mime_type):
        self.mime_type = mime_type
        return self._import

    def _import(self, file_pointer):
        self.file_pointer = file_pointer
        if self._import_return:
            return self._import_return
        else:
            return dict()
