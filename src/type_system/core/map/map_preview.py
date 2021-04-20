from gi.repository import Gtk
import logging

logger = logging.getLogger(__name__)

@Gtk.Template(filename='src/type_system/core/map/map_preview.glade')
class MapPreview(Gtk.Bin):
    """Preview for the core type Map."""

    __gtype_name__ = 'MapPreview'

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (:obj:`MapViewmodel`): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        logger.info('MapPreview created')

    @Gtk.Template.Callback()
    def _click_handler(self, _, __) -> None:
        """Handles clicks on map items, triggers navigation"""
        self._view_model.navigate_to(self._view_model.value)
