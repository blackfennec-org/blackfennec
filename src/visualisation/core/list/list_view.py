from gi.repository import GObject, Gtk
import logging
from src.visualisation.core.list.list_item_view import ListItemView

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/visualisation/core/list/list_view.glade')
class ListView(Gtk.Bin):
    """View for the core type List."""

    __gtype_name__ = 'ListView'
    _item_container: Gtk.Box = Gtk.Template.Child()
    _add_item_row = Gtk.Template.Child()
    _add_popover = Gtk.Template.Child()
    _template_store = Gtk.Template.Child()
    _template_box = Gtk.Template.Child()

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
        item = ListItemView( preview, self._view_model)
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
        value_set = set(new_value.value)
        intersection = self._value.intersection(value_set)
        to_be_added = value_set.difference(intersection)
        for item in to_be_added:
            self._add_item(item)

        to_be_deleted = self._value.difference(intersection)
        for item in to_be_deleted:
            self._remove_item(item)

        self._value = value_set

    def _setup_template_store(self):
        template_store = Gtk.ListStore(GObject.TYPE_STRING)
        templates = self._view_model.get_templates()
        if templates:
            for template in self._view_model.get_templates():
                template_store.append((template.name,))
        else:
            template_store = self._template_store
        self._template_box.set_model(template_store)

    def _get_template_by_string(self, template_string: str):
        for template in self._view_model.get_templates():
            if template.name == template_string:
                return template
        message = f'Template({template_string}) could not be found ' \
                  f'in template registry'
        logger.error(message)
        raise KeyError(message)

    @Gtk.Template.Callback()
    def _add_item_clicked(self, unused_sender, unused_event):
        self._add_popover.set_relative_to(self._add_item_row)
        self._setup_template_store()
        self._add_popover.popup()

    @Gtk.Template.Callback()
    def _add_from_submitted(self, unused_sender):
        self._add_popover.popdown()
        template = self._get_template_by_string(
            self._template_box.get_active_text())
        self._view_model.add_by_template(template)

    @Gtk.Template.Callback()
    def _add_form_canceled(self, unused_sender):
        self._add_popover.popdown()
