class ExtensionSourceRegistryMock:

    def __init__(self, extension_sources=None):
        self._extension_sources = extension_sources\
            if extension_sources else set()
        self.extension_sources_getter_count = 0

        self.register_extension_source_count = 0
        self.register_extension_source_last = None

        self.deregister_extension_source_count = 0
        self.deregister_extension_source_last = None

    @property
    def extension_sources(self):
        self.extension_sources_getter_count += 1
        return self._extension_sources

    def register_extension_source(self, extension_source):
        self.register_extension_source_last = extension_source
        self.register_extension_source_count += 1

    def deregister_extension_source(self, extension_source):
        self.deregister_extension_source_last = extension_source
        self.deregister_extension_source_count += 1
