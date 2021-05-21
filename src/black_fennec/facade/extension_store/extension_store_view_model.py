from typing import List

from src.extension.extension_source import ExtensionSource


class ExtensionStoreViewModel:
    def __init__(self, extension_sources: List[ExtensionSource]):
        self._extension_sources = extension_sources

    @property
    def extensions(self):
        result = list()
        for source in self._extension_sources:
            result += source.extensions
        return result

    def toggle(self, extension):
        if extension.enabled:
            extension.unload()
            extension.enabled = False
        else:
            extension.load()
            extension.enabled = True

    def refresh(self):
        for source in self._extension_sources:
            source.refresh_extensions()
