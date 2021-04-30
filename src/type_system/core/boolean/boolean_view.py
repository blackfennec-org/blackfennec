from gi.repository import Gtk
import logging

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/type_system/core/boolean/boolean_view.glade')
class BooleanView(Gtk.Bin):
    """View for the core type Boolean."""

    __gtype_name__ = 'BooleanView'
    _value = Gtk.Template.Child()

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (:obj:`BooleanViewModel`): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._value.set_state(self._view_model.value)
        logger.info(
            'BooleanView with text: "%s" created', self._view_model.value)
