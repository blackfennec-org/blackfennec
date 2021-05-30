from gi.repository import Gtk, GObject
import logging

from src.visualisation.core.map.map_item_view import MapItemView

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/visualisation/core/map/map_view.glade')
class MapView(Gtk.Bin):
    """View for the core type Map."""

    __gtype_name__ = 'MapView'
    _item_container: Gtk.Box = Gtk.Template.Child()
    _add_item_row = Gtk.Template.Child()
    _add_popover = Gtk.Template.Child()
    _add_entry = Gtk.Template.Child()
    _template_store = Gtk.Template.Child()
    _template_box = Gtk.Template.Child()

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (:obj:`MapViewModel`): The view_model.
        """
        super().__init__()
        self._view_model = view_model

        self._view_model.bind(value=self._update_value)
        self._value_set: set = set()
        self._items: dict = dict()

        self._update_value(self, self._view_model.value)
        logger.info('MapView created')


    def _add_item(self, key, structure):
        preview = self._view_model.create_preview(structure)
        item = MapItemView(
            key, preview,
            self._view_model)
        self._items[key] = item
        self._item_container.add(item)

    def _remove_item(self, key):
        item = self._items.pop(key)
        self._item_container.remove(item)

    def _update_value(self, unused_sender, new_value):
        """Observable handler for value

        Args:
            unused_sender: view model
            new_value: set by view model
        """
        value_set = set(new_value.value)
        intersection = self._value_set.intersection(value_set)
        to_be_added = value_set.difference(intersection)
        for key in to_be_added:
            self._add_item(key, new_value.value[key])
        to_be_deleted = self._value_set.difference(intersection)
        for key in to_be_deleted:
            self._remove_item(key)

        self._value_set = value_set

    def _preview_click_handler(self, unused_sender, route_target) -> None:
        """Handles clicks on map items, triggers navigation"""
        self._view_model.navigate_to(route_target)

    def _delete_request_handler(self, sender):
        self._item_container.remove(sender)
        self._view_model.delete_item(sender.key)

    def _rename_request_handler(self, sender, new_key):
        sender.set_key(new_key)
        self._view_model.rename_key(sender.key, new_key)

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
    def _add_submit_clicked(self, unused_sender):
        key = self._add_entry.get_text()
        self._add_popover.popdown()
        template = self._get_template_by_string(
            self._template_box.get_active_text())
        self._view_model.add_by_template(key, template)
    
    @Gtk.Template.Callback()
    def _cancel_clicked(self, unused_sender):
        self._add_popover.popdown()
