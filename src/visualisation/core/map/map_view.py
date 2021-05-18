from gi.repository import Gtk
import logging

from src.black_fennec.structure.string import String
from src.visualisation.core.map.map_item_view import MapItemView

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/visualisation/core/map/map_view.glade')
class MapView(Gtk.Bin):
    """View for the core type Map."""

    __gtype_name__ = 'MapView'
    _item_container: Gtk.Box = Gtk.Template.Child()

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (:obj:`MapViewModel`): The view_model.
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
                self._delete_request_handler,
                self._rename_request_handler,
                self._add_request_handler,
                self._preview_click_handler)
            self._item_container.add(item)

    def _preview_click_handler(self, unused_sender, route_target) -> None:
        """Handles clicks on map items, triggers navigation"""
        self._view_model.navigate_to(route_target)

    def _delete_request_handler(self, sender):
        self._item_container.remove(sender)
        self._view_model.delete_item(sender.key)

    def _add_request_handler(self, key, template_id):
        substructure = String("")
        self._view_model.add_item(key, substructure)
        preview = self._view_model.create_preview(substructure)
        item = MapItemView(
            key, preview,
            self._delete_request_handler,
            self._rename_request_handler,
            self._add_request_handler,
            self._preview_click_handler)
        self._item_container.add(item)

    def _rename_request_handler(self, sender, new_key):
        sender.set_key(new_key)
        self._view_model.rename_key(sender.key, new_key)

