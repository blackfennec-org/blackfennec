from gi.repository import Gtk
import logging

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/type_system/core/string/string_view.glade')
class StringView(Gtk.Bin):
    """View for the core type String."""

    __gtype_name__ = 'StringView'
    _value = Gtk.Template.Child()

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (:obj:`StringViewModel`): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        buffer = self._value.get_buffer()
        buffer.set_text(self._view_model.value)
        logger.info(
            'StringView with text: "%s" created', self._view_model.value)

    def _on_buffer_changed(self, buffer):
        start, end = buffer.get_bounds()
        text = buffer.get_text(start, end, False)
        self._view_model.value = text
