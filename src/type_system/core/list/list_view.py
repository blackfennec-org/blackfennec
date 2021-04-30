from gi.repository import Gtk
import logging
from src.type_system.core.list.list_item_view import ListItemView

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/type_system/core/list/list_view.glade')
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

        for substructure in self._view_model.value:
            preview = self._view_model.create_preview(substructure)
            item = ListItemView(
                preview,
                self._preview_click_handler)
            self._item_container.add(item)

    def _preview_click_handler(self, unused_sender, route_target) -> None:
        """Handles clicks on list items, triggers navigation"""
        self._view_model.navigate_to(route_target)
