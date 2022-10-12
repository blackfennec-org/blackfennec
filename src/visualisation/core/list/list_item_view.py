import logging
from pathlib import Path

from gi.repository import Gtk, Adw

from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.structure.structure import Structure
from src.visualisation.core.list.list_view_model import ListViewModel

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('list_item_view.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class ListItemView(Adw.ActionRow):
    """View for a single list item."""
    __gtype_name__ = 'ListItemView'
    _preview_container: Gtk.Box = Gtk.Template.Child()

    def __init__(self,
                 preview: Interpretation,
                 view_factory,
                 view_model: ListViewModel):
        """Create list item view

        Args:
            preview (Interpretation): The preview
            view_model (ListViewModel): view model
        """
        super().__init__()

        self._preview = preview
        self._view_model = view_model
        view = view_factory.create(preview)
        self._preview_container.append(view)

    @property
    def item(self) -> Structure:
        """Readonly property for the item"""
        return self._preview.structure

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
