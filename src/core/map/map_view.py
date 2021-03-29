from gi.repository import Gtk
import logging
from src.core.info import Info

logger = logging.getLogger(__name__)

@Gtk.Template(filename='src/core/map/map_view.glade')
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
        for key, value in self._view_model.value.items():
            map_item_view = MapItemView(key, value, self._click_handler)
            self._item_container.add(map_item_view)

    def _click_handler(self, map_item_view) -> None:
        """Handles clicks on map items, triggers navigation"""
        self._view_model.navigate_to(map_item_view.key)

@Gtk.Template(filename='src/core/map/map_item_view.glade')
class MapItemView(Gtk.Bin):
    """View for a key value pair of a map."""
    __gtype_name__ = 'MapItemView'
    _key_label: Gtk.Label = Gtk.Template.Child()

    def __init__(self, key, value: Info, click_handler):
        """Create map item view

        Args:
            key: The key of the map item
            value (:obj:`Info`): The info which should be previewed
            click_handler: A handler that is called when the map item is pressed
        """
        super().__init__()

        self._key = key
        self._value = value
        self._click_handler = click_handler

        self._key_label.set_text(self._key)

    @property
    def key(self) -> str:
        """Readonly property for the key of the item"""
        return self._key

    @Gtk.Template.Callback()
    def on_preview_clicked(self, _) -> None:
        """Callback for the button click event"""
        self._click_handler(self)
