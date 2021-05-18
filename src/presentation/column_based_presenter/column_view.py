import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


@Gtk.Template(filename="src/presentation/column_based_presenter/column_view.glade")
class ColumnView(Gtk.Bin):
    __gtype_name__ = 'ColumnView'
    _paned_right = Gtk.Template.Child()
    _container = Gtk.Template.Child()

    def __init__(self, interpretation):
        super().__init__()
        self._column_right = None
        self._interpretation = interpretation
        self._container.add(interpretation.view)

    def add_column(self, column: 'Column'):
        if self._column_right is None:
            self._paned_right.add(column)
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
