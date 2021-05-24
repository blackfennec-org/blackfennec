import logging

from gi.repository import Gtk, GObject
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.structure.info import Info
from src.visualisation.core.list.list_view_model import ListViewModel

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/visualisation/core/list/list_item_view.glade')
class ListItemView(Gtk.Bin):
    """View for a single list item."""
    __gtype_name__ = 'ListItemView'
    _preview_container: Gtk.Bin = Gtk.Template.Child()
    _popover = Gtk.Template.Child()
    _add_popover = Gtk.Template.Child()
    _template_store = Gtk.Template.Child()
    _template_box = Gtk.Template.Child()

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
    def item(self) -> Info:
        """Readonly property for the item"""
        return self._preview.info

    def on_preview_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        self._view_model.navigate_to(self._preview.info)

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
        elif button == 'Add':
            self._popover.popdown()
            self._add_popover.set_relative_to(self)

            template_store = Gtk.ListStore(GObject.TYPE_STRING)
            templates = self._view_model.get_templates()
            if templates:
                for template in self._view_model.get_templates():
                    template_store.append((template.__str__(),))
            else:
                template_store = self._template_store
            self._template_box.set_model(template_store)

            self._add_popover.popup()
        else:
            message = f'Unknown button({button}) clicked by {sender}'
            logger.warning(message)

    def _delete_request_handler(self, sender):
        self._view_model.delete_item(sender.item)

    @Gtk.Template.Callback()
    def on_add_clicked(self, sender):
        self._add_popover.popdown()
        template = self._get_template_by_string(
            self._template_box.get_active_text()
        )
        self._view_model.add_by_template(template)

    def _get_template_by_string(self, template_string: str):
        for template in self._view_model.get_templates():
            if template.__str__() == template_string:
                return template
        message = f'Template({template_string}) could not be found ' \
                  f'in template registry'
        logger.error(message)
        raise KeyError(message)

    @Gtk.Template.Callback()
    def on_cancel_clicked(self, unused_sender):
        self._add_popover.popdown()

