import logging
from pathlib import Path

from gi.repository import Gtk, Adw

from blackfennec.interpretation.interpretation import Interpretation
from core.list.list_view_model import ListViewModel
from core.util.action_item_view import ActionItemView

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('list_item_view.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class ListItemView(Adw.ActionRow, ActionItemView):
    """View for a single list item."""

    __gtype_name__ = 'ListItemView'

    _popover_parent: Gtk.Box = Gtk.Template.Child()
    _delete = Gtk.Template.Child()

    def __init__(self,
                 interpretation: Interpretation,
                 view_factory,
                 view_model: ListViewModel):
        """Create list item view

        Args:
            interpretation (Interpretation): The preview
            view_model (ListViewModel): view model
        """
        Adw.ActionRow.__init__(self)
        ActionItemView.__init__(self, interpretation, view_model)

        view = next(view_factory.create(interpretation))
        self.set_activatable_widget(view)
        self.add_suffix(view)
        self.add_prefix(self._delete)

    @property
    def action_row(self) -> Adw.ActionRow:
        return self

    @property
    def popover_parent(self) -> Gtk.Box:
        return self._popover_parent

    @Gtk.Template.Callback()
    def _on_delete(self, unused_sender):
        self._view_model.list.remove_item(self._interpretation.structure)

    def set_deletable(self, value: bool):
        self._delete.set_visible(value)
