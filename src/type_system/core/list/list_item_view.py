from gi.repository import Gtk
from src.interpretation.interpretation import Interpretation
from src.structure.info import Info


@Gtk.Template(filename='src/type_system/core/list/list_item_view.glade')
class ListItemView(Gtk.Bin):
    """View for a key value pair of a list."""
    __gtype_name__ = 'ListItemView'
    _key_label: Gtk.label = Gtk.Template.Child()
    _preview_container: Gtk.Bin = Gtk.Template.Child()

    def __init__(self, preview: Interpretation, preview_click_handler):
        """Create list item view

        Args:
            item (:obj:`Info`): The info which should be previewed
            preview_click_handler: A handler that is called when the list item is pressed
        """
        super().__init__()

        self.preview = preview
        self._preview_click_handler = preview_click_handler

        self._key_label.set_text(self._key)
        self._preview_container.add(self._preview.view)

    @property
    def item(self) -> Info:
        """Readonly property for the item"""
        return self._item

    @Gtk.Template.Callback()
    def on_preview_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        self._preview_click_handler(self, self._preview.info)
