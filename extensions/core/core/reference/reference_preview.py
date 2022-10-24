import logging
from pathlib import Path

from gi.repository import Gtk, Adw

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('reference_preview.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class ReferencePreview(Adw.Bin):
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
        logger.info('ReferencePreview created')
        self._reference_value.set_text(str(view_model.reference))

    @Gtk.Template.Callback()
    def _on_navigate(self, unused_sender) -> None:
        """Handles clicks on reference items, triggers navigation"""
        self._view_model.navigate_to_reference()
