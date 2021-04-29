from gi.repository import Gtk
import logging

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/type_system/core/list/list_preview.glade')
class ListPreview(Gtk.Bin):
    """Preview for the core type List"""

    __gtype_name__ = 'ListPreview'

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (:obj:`ListViewmodel`): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        logger.info('ListPreview created')

    @Gtk.Template.Callback()
    def _click_handler(self, unused_sender, unused_argument) -> None:
        """Handles clicks on map items, triggers navigation"""
        self._view_model.navigate_to(self._view_model.value)
