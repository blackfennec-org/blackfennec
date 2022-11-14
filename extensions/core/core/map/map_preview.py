import logging
from pathlib import Path

from gi.repository import Gtk, Adw

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('map_preview.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class MapPreview(Gtk.Button):
    """Preview for the core type Map."""

    __gtype_name__ = 'MapPreview'

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (MapViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        logger.info('MapPreview created')

    @Gtk.Template.Callback()
    def _on_navigate_clicked(self, unused_sender) -> None:
        """Handles clicks on map items, triggers navigation"""
        self._view_model.navigate_to(self._view_model.map)
