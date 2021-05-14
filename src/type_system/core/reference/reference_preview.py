from gi.repository import Gtk
import logging

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/type_system/core/reference/reference_preview.glade')
class ReferencePreview(Gtk.Bin):
    """Preview for the core type Reference."""

    __gtype_name__ = 'ReferencePreview'

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (ReferenceViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        logger.info('ReferencePreview created')

    @Gtk.Template.Callback()
    def _click_handler(self, unused_sender, unused_argument) -> None:
        """Handles clicks on reference items, triggers navigation"""
        self._view_model.navigate_to(self._view_model.reference.destination)
