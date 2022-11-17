from pathlib import Path

from gi.repository import Gtk, Adw
import logging

from blackfennec.util.change_notification import ChangeNotification

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('boolean_view.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class BooleanView(Adw.Bin):
    """View for the core type Boolean."""

    __gtype_name__ = 'BooleanView'
    _value = Gtk.Template.Child()

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (BooleanViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._view_model.bind(changed=self._on_view_model_value_changed)

        self._value.set_state(self._view_model.boolean.value)

    @Gtk.Template.Callback()
    def _on_state_changed(self, unused_sender, state):
        self._view_model.boolean.value = state

    def _on_view_model_value_changed(self, unused_sender, notification: ChangeNotification):
        current_value = self._value.get_state()
        if current_value != notification.new_value:
            self._value.set_state(notification.new_value)
