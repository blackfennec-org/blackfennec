import logging
from pathlib import Path

from gi.repository import Gtk, Adw

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('string_preview.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class StringPreview(Gtk.Frame):
    """View for the core type String."""

    __gtype_name__ = 'StringPreview'
    _value = Gtk.Template.Child()

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (StringViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        buffer = self._value.get_buffer()
        buffer.set_text(self._view_model.value)
        buffer.connect('changed', self._on_buffer_changed)
        self.connect('notify::active', self._on_activate)
        logger.info(
            'StringPreview with text: "%s" created', self._view_model.value)

    def _on_activate(self, unused_sender):
        self._value.activate()

    def _on_buffer_changed(self, buffer):
        start, end = buffer.get_bounds()
        text = buffer.get_text(start, end, False)
        self._view_model.value = text
