from gi.repository import Gtk
from src.core.info import Info

@Gtk.Template(filename='src/core/types/map/map_item_view.glade')
class MapItemView(Gtk.Bin):
    """View for a key value pair of a map."""
    __gtype_name__ = 'MapItemView'
    _key_label: Gtk.Label = Gtk.Template.Child()

    def __init__(self, key, value: Info, preview_click_handler):
        """Create map item view

        Args:
            key: The key of the map item
            value (:obj:`Info`): The info which should be previewed
            click_handler: A handler that is called when the map item is pressed
        """
        super().__init__()

        self._key = key
        self._value = value
        self._preview_click_handler = preview_click_handler

        self._key_label.set_text(self._key)

    @property
    def key(self) -> str:
        """Readonly property for the key of the item"""
        return self._key

    @Gtk.Template.Callback()
    def on_preview_clicked(self, _) -> None:
        """Callback for the button click event"""
        self._preview_click_handler(self, self._value)
