import logging
from gi.repository import Gtk
from src.black_fennec.interpretation.interpretation import Interpretation

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/visualisation/core/map/map_item_view.glade')
class MapItemView(Gtk.Bin):
    """View for a key value pair of a map."""
    __gtype_name__ = 'MapItemView'
    _item_row: Gtk.Box = Gtk.Template.Child()
    _key_label: Gtk.Label = Gtk.Template.Child()
    _preview_container: Gtk.Bin = Gtk.Template.Child()
    _popover = Gtk.Template.Child()
    _edit_popover = Gtk.Template.Child()
    _add_popover = Gtk.Template.Child()
    _rename_entry = Gtk.Template.Child()
    _add_entry = Gtk.Template.Child()
    _liststore = Gtk.Template.Child()

    def __init__(self, key, preview: Interpretation, delete_handler,
                rename_handler, add_handler, preview_click_handler):
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
        self._delete_handler = delete_handler
        self._rename_handler = rename_handler
        self._add_handler = add_handler
        self._preview_click_handler = preview_click_handler

        self.set_key(self._key)
        self._preview_container.add(self._preview.view)

    @property
    def key(self) -> str:
        """Readonly property for the key of the item"""
        return self._key

    def set_key(self, key):
        self._key_label.set_text(key)

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, value):
        self._selected = value
        style = self._item_row.get_style_context()
        if self.selected:
            style.add_class('is-active')
        else:
            style.remove_class('is-active')

    @Gtk.Template.Callback()
    def on_preview_clicked(self, unused_sender) -> None:
        logger.warning('on_preview_clicked is deprecated.')

    @Gtk.Template.Callback()
    def _on_button_click(self, sender, event):
        if event.button != 3:
            return False
        self._popover.set_relative_to(sender)
        self._popover.popup()

    @Gtk.Template.Callback()
    def _on_option_clicked(self, sender):
        button = sender.props.text
        if button == 'Edit':
            self._popover.popdown()
            self._edit_popover.set_relative_to(self)
            self._edit_popover.popup()
        elif button == 'Delete':
            self._delete_handler(self)
        else:
            self._popover.popdown()
            self._add_popover.set_relative_to(self)
            self._add_popover.popup()

    @Gtk.Template.Callback()
    def on_rename_clicked(self, unused_sender):
        new_key = self._rename_entry.get_text()
        self._edit_popover.popdown()
        self._rename_handler(self, new_key)

    @Gtk.Template.Callback()
    def on_add_clicked(self, unused_sender):
        key = self._add_entry.get_text()
        self._add_popover.popdown()
        self._add_handler(key, None)

    @Gtk.Template.Callback()
    def on_cancel_clicked(self, unused_sender):
        self._edit_popover.popdown()
        self._add_popover.popdown()
