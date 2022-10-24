from blackfennec.extension.extension import Extension
from blackfennec.extension.extension_api import ExtensionApi


class ExtensionViewModel:
    def __init__(self, extension: Extension, extension_api: ExtensionApi):
        self._extension = extension
        self._extension_api = extension_api

    @property
    def name(self):
        return self._extension.name

    @property
    def description(self):
        return str(self._extension.location)

    @property
    def enabled(self):
        return self._extension.enabled

    def enable(self):
        self._extension.enabled = True
        self._extension.load(self._extension_api)

    def disable(self):
        self._extension.enabled = False
        self._extension.unload(self._extension_api)
