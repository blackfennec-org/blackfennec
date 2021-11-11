import logging

from gi.repository import Gtk
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.structure.structure import Structure
from src.visualisation.core.list.list_view_model import ListViewModel

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/visualisation/core/list/list_item_view.glade')
class ListItemView(Gtk.Bin):
    """View for a single list item."""
    __gtype_name__ = 'ListItemView'
    _item_row: Gtk.Box = Gtk.Template.Child()
    _preview_container: Gtk.Bin = Gtk.Template.Child()
    _popover = Gtk.Template.Child()

    def __init__(self,
                 preview: Interpretation,
                 view_model: ListViewModel):
        """Create list item view

        Args:
            preview (Interpretation): The preview
            view_model (ListViewModel): view model
        """
        super().__init__()

        self._preview = preview
        self._view_model = view_model

        self._preview_container.add(self._preview.view)

    @property
    def item(self) -> Structure:
        """Readonly property for the item"""
        return self._preview.structure

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

    def on_preview_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        self._view_model.navigate_to(self._preview.structure)

    @Gtk.Template.Callback()
    def _on_button_click(self, sender, event):
        if event.button != 3:
            return False
        self._popover.set_relative_to(sender)
        self._popover.popup()

    @Gtk.Template.Callback()
    def _on_option_clicked(self, sender):
        """Handler for option clicked on popover

        Args:
            sender: popover
        """
        button = sender.props.text
        if button == 'Delete':
            self._delete_request_handler(self)
        else:
            message = f'Unknown button({button}) clicked by {sender}'
            logger.warning(message)

    def _delete_request_handler(self, sender):
        self._view_model.delete_item(sender.item)
