import logging
from gi.repository import Gtk, GObject
from src.black_fennec.interpretation.interpretation import Interpretation
from src.visualisation.core.map.map_view_model import MapViewModel

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/visualisation/core/map/map_item_view.glade')
class MapItemView(Gtk.Bin):
    """View for a key value pair of a map."""
    __gtype_name__ = 'MapItemView'
    _key_label: Gtk.Label = Gtk.Template.Child()
    _preview_container: Gtk.Bin = Gtk.Template.Child()
    _popover = Gtk.Template.Child()
    _edit_popover = Gtk.Template.Child()
    _add_popover = Gtk.Template.Child()
    _rename_entry = Gtk.Template.Child()
    _add_entry = Gtk.Template.Child()
    _template_store = Gtk.Template.Child()
    _template_box = Gtk.Template.Child()


    def __init__(
            self,
            key,
            preview: Interpretation,
            view_model: MapViewModel ):
        """Create map item view.

        Args:
            key: The key of the map item.
            preview (Interpretation): The preview.
            view_model (ListViewModel): view model.

        """
        super().__init__()

        self._key = key
        self._preview = preview
        self._view_model = view_model

        self.set_key(self._key)
        self._preview_container.add(self._preview.view)

    @property
    def key(self) -> str:
        """Readonly property for the key of the item"""
        return self._key

    def set_key(self, key):
        self._key_label.set_text(key)

    @Gtk.Template.Callback()
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
        """Popover click handler

        Args:
            sender: popover
        """
        button = sender.props.text
        if button == 'Edit':
            self._popover.popdown()
            self._edit_popover.set_relative_to(self)
            self._edit_popover.popup()
        elif button == 'Delete':
            self._delete_request_handler(self)
        elif button == 'Add':
            self._popover.popdown()
            self._add_popover.set_relative_to(self)
            self._setup_template_store()
            self._add_popover.popup()
        else:
            message = f'Unknown button({button}) clicked by {sender}'
            logger.warning(message)

    @Gtk.Template.Callback()
    def on_rename_clicked(self, sender):
        new_key = self._rename_entry.get_text()
        self._edit_popover.popdown()
        self._view_model.rename_key(self.key, new_key)

    @Gtk.Template.Callback()
    def on_add_clicked(self, unused_sender):
        key = self._add_entry.get_text()
        self._add_popover.popdown()
        template = self._get_template_by_string(
            self._template_box.get_active_text())
        self._view_model.add_by_template(key, template)

    def _delete_request_handler(self, sender):
        self._view_model.delete_item(sender.key)

    @Gtk.Template.Callback()
    def on_cancel_clicked(self, unused_sender):
        self._edit_popover.popdown()
        self._add_popover.popdown()

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
