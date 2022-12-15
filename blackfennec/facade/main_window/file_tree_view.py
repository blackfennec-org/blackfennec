import os
from gi.repository import Adw, Gtk, Gio

from blackfennec.facade.main_window.black_fennec_view_model import \
    BlackFennecViewModel


def _create_directory_structure(root_directory):
    store = Gtk.TreeStore(str, str)
    parent_map = {root_directory: None}
    for sub_directory, directories, files in os.walk(root_directory):
        for file in files:
            path = os.path.join(sub_directory, file)
            store.append(parent_map[sub_directory], [file, path])
        for directory in directories:
            store_entry = store.append(
                parent_map[sub_directory],
                [directory, 'directory is not a file...']
            )
            path = os.path.join(sub_directory, directory)
            parent_map[path] = store_entry
    return store


class FileTreeView:

    def __init__(
            self,
            tree_view: Gtk.TreeView,
            view_model: BlackFennecViewModel
    ):
        self._tree_view: Gtk.TreeView = tree_view
        self._view_model: BlackFennecViewModel = view_model

        renderer = Gtk.CellRendererText()
        tree_view_column = Gtk.TreeViewColumn(
            'Current directory', renderer, text=0)
        self._tree_view.append_column(tree_view_column)

        self._tree_view.connect('row-activated', self._on_row_activated)

    def load_directory(self, directory_location: str):
        store = _create_directory_structure(directory_location)
        self._tree_view.set_model(store)

    def _on_row_activated(
            self,
            unused_sender,
            path,
            unused_column
    ) -> None:
        model = self._tree_view.get_model()
        iterator = model.get_iter(path)
        if iterator:
            uri = model.get_value(iterator, 1)
            self._view_model.open_file(uri)
