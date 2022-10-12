from pathlib import Path

from gi.repository import Gtk, Adw

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('column_view.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class ColumnView(Adw.Bin):
    """View for a single column for the column-based presenter
    """
    __gtype_name__ = 'ColumnView'
    _paned_right = Gtk.Template.Child()
    _container: Gtk.ScrolledWindow = Gtk.Template.Child()

    def __init__(self, interpretation, view_factory):
        super().__init__()
        self._column_right = None
        self._interpretation = interpretation
        view = view_factory.create(interpretation)
        self._container.set_child(view)

    def add_column(self, column: 'Column'):
        if self._column_right is None:
            self._paned_right.append(column)
            self._column_right = column
        else:
            self._column_right.add_column(column)

    def i_host_interpretation(self, interpretation):
        return self._interpretation == interpretation

    def remove_column(self, interpretation):
        if self._column_right.i_host_interpretation(interpretation):
            self._paned_right.remove(self._column_right)
            self._column_right = None
        else:
            self._column_right.remove_column(interpretation)
