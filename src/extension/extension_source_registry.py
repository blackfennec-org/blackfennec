from typing import Set

from src.extension.extension_source import ExtensionSource


class ExtensionSourceRegistry:
    """Extension Source Registry Class

    Is a register of all known or registered extension_sources.

    Attributes:
        _extension_sources: stores internal extension_sources
    """

    def __init__(self):
        """ Extension Source Registry constructor.

        Initializes extension sources with empty set
        """
        self._extension_sources = set()

    @property
    def extension_sources(self) -> Set[ExtensionSource]:
        """extension_sources getter

            Returns:
                set: of extension_source_bidder
        """
        return set(self._extension_sources)

    def register_extension_source(self, extension_source: ExtensionSource):
        """Function to register a new extension source

            Args:
                extension_source (ExtensionSource): future element of the extension source list
        """
        self._extension_sources.add(extension_source)

    def deregister_extension_source(self, extension_source: ExtensionSource):
        """Function to deregister a extension_source from the registry

        Args:
            extension_source (ExtensionSource): element in the extension source registry

        """
        self._extension_sources.remove(extension_source)
