from gi.repository import Gtk
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
        self._view_model.bind(value=self._update_value)
        self._value: set = set()
        self._items: dict = dict()

        self._populate_items()
        logger.info('ListView created')

    def _populate_items(self) -> None:
        """Populates the list that displays the list items"""

        for substructure in self._view_model.value.value:
            self._add_item(substructure)

        self._value = set(self._view_model.value.value)

    def _add_item(self, structure):
        preview = self._view_model.create_preview(structure)
        item = ListItemView(
            preview,
            self._view_model
        )
        self._items[structure] = item
        self._item_container.add(item)

    def _remove_item(self, structure):
        item = self._items[structure]
        self._items.pop(structure)
        self._item_container.remove(item)

    def _update_value(self, unused_sender, new_value):
        """Observable handler for value

        Args:
            unused_sender: view model
            new_value: set by view model
        """
        value_set = set(new_value)
        intersection = self._value.intersection(value_set)
        to_be_added = value_set.difference(intersection)
        for item in to_be_added:
            self._add_item(item)

        to_be_deleted = self._value.difference(intersection)
        for item in to_be_deleted:
            self._remove_item(item)

        self._value = value_set
