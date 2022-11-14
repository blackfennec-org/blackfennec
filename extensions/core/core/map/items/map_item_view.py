import logging
from pathlib import Path

from gi.repository import Gtk, Adw, Gio, Gdk

from blackfennec.interpretation.interpretation import Interpretation
from core.map.map_view_model import MapViewModel
from core.util.action_item_view import ActionItemView

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('map_item_view.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class MapItemView(Adw.ActionRow, ActionItemView):
    """View for a key value pair of a map."""

    __gtype_name__ = 'MapItemView'

    _popover_parent: Gtk.Box = Gtk.Template.Child()

    def __init__(
            self,
            key,
            interpretation: Interpretation,
            view_factory,
            view_model: MapViewModel
    ):
        """Create map item view.

        Args:
            key: The key of the map item.
            interpretation (Interpretation): The preview.
            view_model (ListViewModel): view model.

        """
        Adw.ActionRow.__init__(self)
        ActionItemView.__init__(self, interpretation, view_model)
        self.key = key

        view = next(view_factory.create(interpretation))
        self.set_activatable_widget(view)
        self.add_suffix(view)

    @property
    def action_row(self) -> Adw.ActionRow:
        return self

    @property
    def popover_parent(self) -> Gtk.Box:
        return self._popover_parent

    @property
    def key(self) -> str:
        """Readonly property for the key of the item"""
        return self._key

    @key.setter
    def key(self, key):
        self._key = key
        self.set_title(key)
