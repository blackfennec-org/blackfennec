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

    def __init__(self, view_factory, view_model):
        """Construct with view_model.

        Args:
            view_model (ListViewModel): The view_model.
        """
        super().__init__()
        self._value: list = []
        self._items: dict = {}
        self._item_interpretation_mapping = {}
        self._currently_selected = None
        self._view_factory = view_factory
        self._view_model = view_model
        self._view_model.bind(
            value=self._update_value,
            selected=self._on_selection_changed)

        self._update_value(self, self._view_model.value)
        logger.info('ListView created')

    def _add_item(self, structure):
        preview = self._view_model.create_preview(structure)
        item = ListItemView(
            preview,
            self._view_factory,
            self._view_model)
        self._items[structure] = item
        self._item_container.add(item)
        self._item_interpretation_mapping[preview] = item

    def _remove_item(self, structure):
        item = self._items[structure]
        self._items.pop(structure)
        self._item_container.remove(item)

    def _set_item_position(self, key, position):
        item = self._items[key]
        self._item_container.reorder_child(item, position)

    def _update_value(self, unused_sender, new_value):
        """Observable handler for value

        Args:
            unused_sender: view model
            new_value: set by view model
        """
        for item in self._value:
            if item not in new_value.value:
                self._remove_item(item)

        for i, item in enumerate(new_value.value):
            if item not in self._value:
                self._add_item(item)
            self._set_item_position(item, i)
        self._value = new_value.value

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

    def _preview_click_handler(
            self,
            unused_sender,
            unused_route_target) -> None:
        logger.warning('preview clicked handler is deprecated')

    def _on_selection_changed(self, unused_sender, new_value):
        if self._currently_selected:
            self._currently_selected.selected = False
        self._currently_selected = self._find_by_interpretation(new_value)
        if self._currently_selected:
            self._currently_selected.selected = True

    def _find_by_interpretation(self, structure):
        if structure in self._item_interpretation_mapping:
            return self._item_interpretation_mapping[structure]
        return None

    @Gtk.Template.Callback()
    def _add_item_clicked(self, unused_sender):
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
