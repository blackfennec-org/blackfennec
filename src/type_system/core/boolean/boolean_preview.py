from gi.repository import Gtk
import logging

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/type_system/core/boolean/boolean_preview.glade')
class BooleanPreview(Gtk.Bin):
    """View for the core type Boolean."""

    __gtype_name__ = 'BooleanPreview'
    _value = Gtk.Template.Child()

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (:obj:`BooleanViewmodel`): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        buffer = self._value.get_buffer()
        buffer.set_text(self._view_model.value)
        logger.info(
            'BooleanPreview with text: "%s" created', self._view_model.value)
