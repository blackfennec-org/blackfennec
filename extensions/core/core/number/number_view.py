from pathlib import Path

from gi.repository import Gtk, Adw
import logging

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('number_view.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class NumberView(Adw.Bin):
    """View for the core type Number."""

    __gtype_name__ = 'NumberView'
    _value = Gtk.Template.Child()

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (NumberViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._value.set_text(str(self._view_model.value))
        logger.info(
            'NumberView with text: "%s" created', self._view_model.value)
