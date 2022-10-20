import logging
from pathlib import Path

from gi.repository import GObject, Gtk, Adw

from src.visualisation.core.list.list_item_view import ListItemView
from src.black_fennec.structure.structure import Structure

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('list_view.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class ListView(Adw.Bin):
    """View for the core type List."""

    __gtype_name__ = 'ListView'
    _preference_group: Adw.PreferencesGroup = Gtk.Template.Child()

    _add_popover: Gtk.Popover = Gtk.Template.Child()
    _template_store: Gtk.ListStore = Gtk.Template.Child()
    _template_box = Gtk.Template.Child()

    _edit_suffix_group: Gtk.Box = Gtk.Template.Child()
    _edit: Gtk.Button = Gtk.Template.Child()

    def __init__(self, view_factory, view_model):
        """Construct with view_model.

        Args:
            view_model (ListViewModel): The view_model.
        """
        super().__init__()
        self._value: list = []
        self._items: list[ListItemView] = []
        self._item_interpretation_mapping = {}
        self._currently_selected = None
        self._view_factory = view_factory
        self._view_model = view_model
        self._in_edit_mode = False
        self._view_model.bind(
            value=self._update_value,
            selected=self._on_selection_changed)

        self._update_value(self, self._view_model.value)
        self._setup_template_store()

    @Gtk.Template.Callback()
    def _on_edit(self, unused_sender):
        assert not self._in_edit_mode, 'edit mode already active'

        self._in_edit_mode = True
        self._edit_suffix_group.set_visible(True)
        self._edit.set_visible(False)

        self._update_value(self, self._view_model.decapsulated_value)

    @Gtk.Template.Callback()
    def _on_apply(self, unused_sender):
        assert self._in_edit_mode, 'edit mode not active'

        self._in_edit_mode = False
        self._edit_suffix_group.set_visible(False)
        self._edit.set_visible(True)

        self._update_value(self, self._view_model.value)

    @Gtk.Template.Callback()
    def _on_delete(self, unused_sender):
        self._view_model.delete()

    def _add_item(self, structure):
        preview = self._view_model.create_preview(structure)
        item = ListItemView(
            preview,
            self._view_factory,
            self._view_model)
        item.set_deletable(self._in_edit_mode)
        self._items.append(item)
        self._preference_group.add(item)
        self._item_interpretation_mapping[preview] = item

    def _update_value(self, unused_sender, new_value):
        """Observable handler for value

        Args:
            unused_sender: view model
            new_value: set by view model
        """
        currently_selected_index = 0
        for index, item in enumerate(self._items):
            if item is self._currently_selected:
                currently_selected_index = index
            self._preference_group.remove(item)
        self._items = []
        for structure in new_value.value:
            self._add_item(structure)

        if currently_selected_index >= len(self._items):
            currently_selected_index = len(self._items) - 1
        self._items[currently_selected_index].activate()

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
    def _add_list_item(self, unused_sender):
        self._add_popover.popdown()
        template = self._get_template_by_string(
            self._template_box.get_active_text())
        self._view_model.add_by_template(template)
