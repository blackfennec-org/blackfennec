import logging
from pathlib import Path

from gi.repository import Gtk, Adw
from src.black_fennec.interpretation.interpretation import Interpretation
from src.visualisation.core.map.map_view_model import MapViewModel

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('editable_item_view.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class EditableItemView(Adw.EntryRow):
    """View for a key value pair of a map."""
    __gtype_name__ = 'EditableItemView'

    def __init__(
            self,
            key,
            preview: Interpretation,
            view_factory,
            view_model: MapViewModel):
        """Create map item view.

        Args:
            key: The key of the map item.
            preview (Interpretation): The preview.
            view_model (ListViewModel): view model.

        """
        super().__init__()

        self._key = key
        self._preview = preview
        self._view_model = view_model

        self.key = self._key
        view = view_factory.create(preview)
        self.add_suffix(view)

    @property
    def key(self) -> str:
        """Readonly property for the key of the item"""
        return self._key

    @key.setter
    def key(self, key):
        self._key = key
        self.set_text(key)

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, value):
        self._selected = value
        style = self.get_style_context()
        if self.selected:
            style.add_class('is-active')
        else:
            style.remove_class('is-active')

    @Gtk.Template.Callback()
    def _on_apply(self, sender):
        new_key = sender.get_text()
        self._view_model.rename_key(self.key, new_key)
        self._key = new_key

    @Gtk.Template.Callback()
    def _on_delete(self, unused_sender):
        self._view_model.delete_item(self.key)
