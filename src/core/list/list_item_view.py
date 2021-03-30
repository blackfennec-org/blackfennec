from gi.repository import Gtk
from src.core.info import Info

@Gtk.Template(filename='src/core/list/list_item_view.glade')
class ListItemView(Gtk.Bin):
    """View for a key value pair of a list."""
    __gtype_name__ = 'ListItemView'

    def __init__(self, item: Info, click_handler):
        """Create list item view

        Args:
            item (:obj:`Info`): The info which should be previewed
            click_handler: A handler that is called when the map item is pressed
        """
        super().__init__()

        self._item = item
        self._click_handler = click_handler

    @property
    def item(self) -> Info:
        """Readonly property for the item"""
        return self._item

    @Gtk.Template.Callback()
    def on_preview_clicked(self, _) -> None:
        """Callback for the button click event"""
        self._click_handler(self)
