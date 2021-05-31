from gi.repository import Gtk
import logging
from uri import URI

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/visualisation/core/reference/reference_preview.glade')
class ReferencePreview(Gtk.Bin):
    """Preview for the core type Reference."""

    __gtype_name__ = 'ReferencePreview'
    _reference_value = Gtk.Template.Child()

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (ReferenceViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._update_reference_value()
        logger.info('ReferencePreview created')

    def _update_reference_value(self):
        value = self._view_model.reference.value.uri
        self._reference_value.set_text(value)

    @Gtk.Template.Callback()
    def _click_handler(self, unused_sender, unused_argument) -> None:
        """Handles clicks on reference items, triggers navigation"""
        self._view_model.navigate_to(self._view_model.reference.destination)

    @Gtk.Template.Callback()
    def _on_text_changed(self, unused_sender):
        reference = self._reference_value.get_text()
        self._view_model.reference.value = URI(reference)
