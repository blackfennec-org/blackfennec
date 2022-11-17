import logging
from pathlib import Path

from gi.repository import Gtk, Adw

from blackfennec.util.change_notification import ChangeNotification

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('string_view.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class StringView(Adw.Bin):
    """View for the core type String."""

    __gtype_name__ = 'StringView'
    _value = Gtk.Template.Child()

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (StringViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._view_model.bind(changed=self._update_value)

        buffer = self._value.get_buffer()
        buffer.connect('changed', self._on_text_changed)
        buffer.set_text(self._view_model.string.value)
        logger.info(
            'StringView with text: "%s" created', self._view_model.string.value)

    def _on_text_changed(self, buffer):
        start, end = buffer.get_bounds()
        text = buffer.get_text(start, end, False)
        self._view_model.string.value = text

    def _update_value(self, unused_sender, notification: ChangeNotification):
        buffer = self._value.get_buffer()
        buffer.set_text(notification.new_value)
