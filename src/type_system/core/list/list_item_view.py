from gi.repository import Gtk
from src.interpretation.interpretation import Interpretation
from src.structure.info import Info


@Gtk.Template(filename='src/type_system/core/list/list_item_view.glade')
class ListItemView(Gtk.Bin):
    """View for a single list item."""
    __gtype_name__ = 'ListItemView'
    _preview_container: Gtk.Bin = Gtk.Template.Child()
    _popover = Gtk.Template.Child()
    _add_popover = Gtk.Template.Child()

    def __init__(self,
            preview: Interpretation,
            delete_handler,
            add_handler,
            preview_click_handler):
        """Create list item view

        Args:
            preview (:obj:`Interpretation`): The preview
            preview_click_handler: A handler that is called
                when the list item is pressed
        """
        super().__init__()

        self._preview = preview
        self._delete_handler = delete_handler
        self._add_handler = add_handler
        self._preview_click_handler = preview_click_handler

        self._preview_container.add(self._preview.view)

    @property
    def item(self) -> Info:
        """Readonly property for the item"""
        return self._preview.info

    @Gtk.Template.Callback()
    def on_preview_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        self._preview_click_handler(self, self._preview.info)

    @Gtk.Template.Callback()
    def _on_button_click(self, sender, event):
        if event.button != 3:
            return False
        self._popover.set_relative_to(sender)
        self._popover.popup()

    @Gtk.Template.Callback()
    def _on_option_clicked(self, sender):
        button = sender.props.text
        if button == 'Delete':
            self._delete_handler(self)
        else:
            self._popover.popdown()
            self._add_popover.set_relative_to(self)
            self._add_popover.popup()

    @Gtk.Template.Callback()
    def on_add_clicked(self, unused_sender):
        self._add_popover.popdown()
        self._add_handler(None)

    @Gtk.Template.Callback()
    def on_cancel_clicked(self, unused_sender):
        self._add_popover.popdown()

