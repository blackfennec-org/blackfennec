from pathlib import Path
from core.string.string_view_model import StringViewModel

from gi.repository import Gtk, Adw

from blackfennec.util.change_notification import ChangeNotification

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('string_view.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class StringView(Adw.Bin):
    """View for the core type String."""

    __gtype_name__ = 'StringView'
    _value = Gtk.Template.Child()

    def __init__(self, view_model: StringViewModel):
        """Construct with view_model.

        Args:
            view_model (StringViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._view_model.bind(changed=self._update_value)
        self._buffer_listener_paused = False

        buffer = self._value.get_buffer()
        buffer.set_text(self._view_model.string.value)
        buffer.set_enable_undo(False)
        buffer.connect('changed', self._on_buffer_changed)
        self.connect('notify::active', self._on_activate)

    @property
    def text(self):
        buffer = self._value.get_buffer()
        start, end = buffer.get_bounds()
        return buffer.get_text(start, end, False)

    @text.setter
    def text(self, text):
        buffer = self._value.get_buffer()
        self._buffer_listener_paused = True
        start, end = buffer.get_bounds()
        if buffer.get_text(start, end, False) == text:
            return
        buffer.set_text(text, len(text))

    def _on_activate(self, unused_sender):
        self._value.activate()

    def _on_buffer_changed(self, buffer):
        # This is a workaround for a bug in Gtk.TextView
        #   when we set the text in the buffer, the buffer-changed signal is
        #   emitted, twice. The first time with an empty string.

        if self._buffer_listener_paused:
            self._buffer_listener_paused = False
            return

        self._view_model.value = self.text

    def _update_value(self, unused_sender, notification: ChangeNotification):
        self.text = notification.new_value
