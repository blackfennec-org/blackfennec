class ExtensionSourceMock:
    def __init__(self, extensions=None):
        self.extensions = extensions if extensions else set()
        self.refresh_extensions_count = 0
        self.extensions_getter_count = 0

    def refresh_extensions(self):
        self.refresh_extensions_count += 1
