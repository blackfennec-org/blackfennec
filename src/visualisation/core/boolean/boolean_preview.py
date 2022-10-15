import logging
from pathlib import Path

from gi.repository import Gtk, Adw

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('boolean_preview.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class BooleanPreview(Gtk.Switch):
    """View for the core type Boolean."""

    __gtype_name__ = 'BooleanPreview'

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (BooleanViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self.set_state(self._view_model.value)

        logger.info(
            'BooleanView with text: "%s" created', self._view_model.value)

    @Gtk.Template.Callback()
    def _on_state_changed(self, unused_sender, state):
        self._view_model.value = state
