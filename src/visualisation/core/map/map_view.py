import logging
from pathlib import Path

from gi.repository import Gtk, GObject, Adw

from src.visualisation.core.map.items.action_item_view import ActionItemView
from src.visualisation.core.map.items.editable_item_view import EditableItemView

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('map_view.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class MapView(Adw.Bin):
    """View for the core type Map."""

    __gtype_name__ = 'MapView'
    _preference_group: Gtk.Box = Gtk.Template.Child()
    _add_popover = Gtk.Template.Child()
    _add_entry = Gtk.Template.Child()
    _template_store = Gtk.Template.Child()
    _template_box = Gtk.Template.Child()

    _edit_suffix_group = Gtk.Template.Child()
    _edit = Gtk.Template.Child()

    def __init__(self, view_factory, view_model):
        """Construct with view_model.

        Args:
            view_model (MapViewModel): The view_model.
        """
        super().__init__()
        self._value: dict = {}
        self._items: dict = {}
        self._item_interpretation_mapping = {}
        self._currently_selected = None
        self._view_factory = view_factory
        self._view_model = view_model
        self._view_model.bind(
            value=self._update_value,
            selected=self._on_selection_changed)

        self._in_edit_mode = False
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

    @Gtk.Template.Callback()
    def _on_add_by_template(self, unused_sender):
        key = self._add_entry.get_text()
        self._add_popover.popdown()
        template = self._get_template_by_string(
            self._template_box.get_active_text())
        self._view_model.add_by_template(key, template)

    def _add_item(self, key, structure):
        preview = self._view_model.create_preview(structure)
        if self._in_edit_mode:
            item = EditableItemView(
                key,
                preview,
                self._view_factory,
                self._view_model
            )
        else:
            item = ActionItemView(
                key,
                preview,
                self._view_factory,
                self._view_model
            )
        self._items[key] = item
        self._item_interpretation_mapping[preview] = item
        self._preference_group.add(item)

    def _remove_item(self, key):
        item = self._items.pop(key)
        self._preference_group.remove(item)

    def _update_value(self, unused_sender, new_value):
        """Observable handler for value

        Args:
            unused_sender: view model
            new_value: set by view model
        """
        for key in self._value:
            self._remove_item(key)
        for key, value in new_value.value.items():
            self._add_item(key, value)
        self._value = new_value.value

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
