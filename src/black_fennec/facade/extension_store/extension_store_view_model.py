from src.black_fennec.util.observable import Observable
from src.extension.extension_api import ExtensionApi
from src.extension.extension_source_registry import ExtensionSourceRegistry


class ExtensionStoreViewModel(Observable):
    def __init__(
            self,
            extension_source_registry: ExtensionSourceRegistry,
            extension_api: ExtensionApi
    ):
        Observable.__init__(self)
        self._extension_source_registry = extension_source_registry
        self._extension_api = extension_api
        self._extensions: set = set()
        self.reload_extensions()

    def reload_extensions(self):
        self._extensions = set()
        for source in self._extension_source_registry.extension_sources:
            self._extensions.update(source.extensions)
        self._notify(self._extensions, 'extensions')

    @property
    def extension_api(self) -> ExtensionApi:
        return self._extension_api

    @property
    def extensions(self) -> set:
        return self._extensions

    def reload_extension_from_source(self):
        for source in self._extension_source_registry.extension_sources:
            source.refresh_extensions()
