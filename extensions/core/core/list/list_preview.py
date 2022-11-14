from pathlib import Path

from gi.repository import Gtk, Adw
import logging

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('list_preview.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class ListPreview(Gtk.Button):
    """Preview for the core type List"""

    __gtype_name__ = 'ListPreview'

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (ListViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        logger.info('ListPreview created')

    @Gtk.Template.Callback()
    def _on_navigate_clicked(self, unused_sender) -> None:
        """Handles clicks on list items, triggers navigation"""
        self._view_model.navigate_to(self._view_model.list)
