from gi.repository import Gtk
import logging

logger = logging.getLogger(__name__)

@Gtk.Template(filename='src/core/string/string_view.glade')
class StringView(Gtk.Bin):
    """View for the core type String."""

    __gtype_name__ = 'StringView'
    _value = Gtk.Template.Child()

    def __init__(self, viewmodel):
        """Construct with viewmodel.

        Args:
            viewmodel (:obj:`StringViewmodel`): The viewmodel.
        """
        super().__init__()
        self._viewmodel = viewmodel
        buffer = self._value.get_buffer()
        buffer.set_text(self._viewmodel.value)
        logger.info(
            'StringView with text: "%s" created', viewmodel.value)
