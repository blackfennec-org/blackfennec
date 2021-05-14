from gi.repository import Gtk
from src.interpretation.interpretation import Interpretation


@Gtk.Template(filename='src/type_system/core/map/map_item_view.glade')
class MapItemView(Gtk.Bin):
    """View for a key value pair of a map."""
    __gtype_name__ = 'MapItemView'
    _key_label: Gtk.Label = Gtk.Template.Child()
    _preview_container: Gtk.Bin = Gtk.Template.Child()

    def __init__(self, key, preview: Interpretation, preview_click_handler):
        """Create map item view

        Args:
            key: The key of the map item
            preview (:obj:`Interpretation`): The preview
            preview_click_handler: A handler that is called when
            the map item is pressed
        """
        super().__init__()

        self._key = key
        self._preview = preview
        self._preview_click_handler = preview_click_handler

        self._key_label.set_text(self._key)
        self._preview_container.add(self._preview.view)

    @property
    def key(self) -> str:
        """Readonly property for the key of the item"""
        return self._key

    @Gtk.Template.Callback()
    def on_preview_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""

        print('_preview_click_handler')
        self._preview_click_handler(self, self._preview.info)

    @Gtk.Template.Callback()
    def _on_button_click(self, sender, widget):
        print('_on_button_click')
        self.popover = Gtk.Popover()
        self.popover.set_relative_to(sender)
        self.popover.show()

    """
        if event.type == Gdk.EventType.BUTTON_PRESS and event.button == 3:
            self.popup.popup(None, None, None, None, event.button, event.time)
            return True  # event has been handled
    """
