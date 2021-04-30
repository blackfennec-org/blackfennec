from gi.repository import Gtk
import logging

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/type_system/core/number/number_preview.glade')
class NumberPreview(Gtk.Bin):
    """View for the core type Number"""

    __gtype_name__ = 'NumberPreview'
    _value = Gtk.Template.Child()

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (:obj:`NumberViewmodel`): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._value.set_text(str(self._view_model.value))
        logger.info(
            'NumberView with text: "%s" created', self._view_model.value)
