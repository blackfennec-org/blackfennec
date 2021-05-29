from gi.repository import Gtk
import logging

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

        self._view_model.bind(value=self._update_value)
        self._value_set: set = set()
        self._items: dict = dict()

        self._update_value(self, self._view_model.value)
        logger.info('MapView created')


    def _add_item(self, key, structure):
        preview = self._view_model.create_preview(structure)
        item = MapItemView(
            key, preview,
            self._view_model)
        self._items[key] = item
        self._item_container.add(item)

    def _remove_item(self, key):
        item = self._items.pop(key)
        self._item_container.remove(item)

    def _update_value(self, unused_sender, new_value):
        """Observable handler for value

        Args:
            unused_sender: view model
            new_value: set by view model
        """
        value_set = set(new_value.value)
        intersection = self._value_set.intersection(value_set)
        to_be_added = value_set.difference(intersection)
        for key in to_be_added:
            self._add_item(key, new_value.value[key])
        to_be_deleted = self._value_set.difference(intersection)
        for key in to_be_deleted:
            self._remove_item(key)

        self._value_set = value_set

    def _preview_click_handler(self, unused_sender, route_target) -> None:
        """Handles clicks on map items, triggers navigation"""
        self._view_model.navigate_to(route_target)

    def _delete_request_handler(self, sender):
        self._item_container.remove(sender)
        self._view_model.delete_item(sender.key)

    def _rename_request_handler(self, sender, new_key):
        sender.set_key(new_key)
        self._view_model.rename_key(sender.key, new_key)

