import logging
from pathlib import Path

from gi.repository import Gtk, Adw

from blackfennec.util.change_notification import ChangeNotification

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
        self._view_model.bind(changed=self._on_view_model_value_changed)

        self.set_state(self._view_model.boolean.value)

    @Gtk.Template.Callback()
    def _on_state_changed(self, unused_sender, state):
        self._view_model.boolean.value = state

    def _on_view_model_value_changed(self, unused_sender, notification: ChangeNotification):
        self.set_state(notification.new_value)
