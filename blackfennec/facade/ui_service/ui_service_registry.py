from gi.repository import Gtk

from blackfennec.facade.ui_service.ui_service import UiService


class UiServiceRegistry:
    """Registry for UI services."""
    def __init__(self):
        self._services = {}

    @property
    def services(self) -> dict[Gtk.Window, UiService]:
        """Get UI services."""
        return dict(self._services)

    def register(self, window=Gtk.Window, service=UiService):
        """Register a UI service."""
        self._services[window] = service

    def unregister(self, window=Gtk.Window):
        """Unregister a UI service."""
        del self._services[window]
