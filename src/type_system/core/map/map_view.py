from gi.repository import Gtk
import logging
from src.type_system.core.map.map_item_view import MapItemView

logger = logging.getLogger(__name__)

@Gtk.Template(filename='src/type_system/core/map/map_view.glade')
class MapView(Gtk.Bin):
    """View for the core type Map."""

    __gtype_name__ = 'MapView'
    _item_container: Gtk.Box = Gtk.Template.Child()

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (:obj:`MapViewmodel`): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._populate_items()
        logger.info('MapView created')

    def _populate_items(self) -> None:
        """Populates the list that displays the map items"""
        for key, substructure in self._view_model.value.items():
            preview = self._view_model.create_preview(substructure)
            item = MapItemView(
                key, preview,
                self._preview_click_handler)
            self._item_container.add(item)

    def _preview_click_handler(self, _, route_target) -> None:
        """Handles clicks on map items, triggers navigation"""
        self._view_model.navigate_to(route_target)
