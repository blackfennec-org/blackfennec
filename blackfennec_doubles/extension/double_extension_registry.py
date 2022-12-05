

class ExtensionRegistryMock:
    def __init__(self) -> None:
        self._registry = set()

    def register(self, extension):
        self._registry.add(extension)

    def get_extensions(self) -> list:
        return self._registry
