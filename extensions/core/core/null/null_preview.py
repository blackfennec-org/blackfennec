import logging
from pathlib import Path

from gi.repository import Gtk, Adw

from core.null.null_view_model import NullViewModel

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('null_preview.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class NullPreview(Adw.Bin):
    """Preview for the core type Map."""

    __gtype_name__ = 'NullPreview'
    _value = Gtk.Template.Child()

    def __init__(self, view_model: NullViewModel):
        """Construct with view_model.

        Args:
            view_model (NullViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._value.set_text('None')
        logger.info('NullPreview created')
