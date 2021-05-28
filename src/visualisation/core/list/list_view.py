from gi.repository import Gtk
from src.black_fennec.structure.string import String
import logging
from src.visualisation.core.list.list_item_view import ListItemView

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/visualisation/core/list/list_view.glade')
class ListView(Gtk.Bin):
    """View for the core type List."""

    __gtype_name__ = 'ListView'
    _item_container: Gtk.Box = Gtk.Template.Child()

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (ListViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._populate_items()
        logger.info('ListView created')

    def _populate_items(self) -> None:
        """Populates the list that displays the list items"""

        for substructure in self._view_model.value.value:
            self._add_item(substructure)

    def _add_item(self, structure):
        preview = self._view_model.create_preview(structure)
        item = ListItemView(
            preview,
            self._delete_request_handler,
            self._add_request_handler,
            self._preview_click_handler)
        self._item_container.add(item)

    def _preview_click_handler(self, unused_sender, route_target) -> None:
        """Handles clicks on list items, triggers navigation"""
        self._view_model.navigate_to(route_target)

    def _delete_request_handler(self, sender):
        self._item_container.remove(sender)
        self._view_model.delete_item(sender.item)

    def _add_request_handler(self, template_id):
        structure = String('')
        self._view_model.add_item(structure)
        self._add_item(structure)

    def _rename_request_handler(self, sender, new_key):
        sender.set_key(new_key)
        self._view_model.rename_key(sender.key, new_key)
