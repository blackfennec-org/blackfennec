

from blackfennec.extension_system.extension import Extension


class ExtensionRegistry:
    def __init__(self) -> None:
        self._registry = set()

    def register(self, extension: Extension):
        self._registry.add(extension)

    def get_extensions(self) -> list[Extension]:
        return list(self._registry)
