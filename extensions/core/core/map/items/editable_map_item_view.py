import logging
from pathlib import Path

from gi.repository import Gtk, Adw
from blackfennec.interpretation.interpretation import Interpretation
from core.map.map_view_model import MapViewModel

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('editable_map_item_view.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class EditableMapItemView(Adw.EntryRow):
    """View for a key value pair of a map."""
    __gtype_name__ = 'EditableItemView'

    _delete = Gtk.Template.Child()

    def __init__(
            self,
            key,
            interpretation: Interpretation,
            view_factory,
            view_model: MapViewModel):
        """Create map item view.

        Args:
            key: The key of the map item.
            interpretation (Interpretation): The preview.
            view_model (ListViewModel): view model.

        """
        super().__init__()

        self._key = key
        self._preview = interpretation
        self._view_model = view_model

        self.key = self._key
        view = next(view_factory.create(interpretation))
        self.add_prefix(self._delete)
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
            style.add_class('card')
        else:
            style.remove_class('card')

    @Gtk.Template.Callback()
    def _on_apply(self, sender):
        new_key = sender.get_text()
        self._view_model.map.rename_key(self.key, new_key)
        self._key = new_key

    @Gtk.Template.Callback()
    def _on_delete(self, unused_sender):
        self.selected = False
        self._view_model.selected = None
        self._view_model.map.remove_item(self.key)
