import tempfile

from uri import URI


class UriLoadingStrategyFactoryMock:
    def __init__(self, load_return = None):
        self.uri = None
        self.current_path = None
        self.mime_type = None
        self.create_count = 0
        self._load_return = load_return

    def create(self, uri: URI):
        return self._load

    def _load(self, uri, current_path, mime_type):
        self.uri = uri
        self.current_path = current_path
        self.mime_type = mime_type
        if self._load_return:
            return self._load_return
        else:
            tempfile.TemporaryFile()
