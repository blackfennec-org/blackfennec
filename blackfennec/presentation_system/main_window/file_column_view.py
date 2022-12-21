import os
from pathlib import Path

from gi.repository import Gtk, GObject, Gio

from blackfennec.presentation_system.main_window.black_fennec_view_model import \
    BlackFennecViewModel


class FileEntry(GObject.Object):
    __gtype_name__ = "FileEntry"

    def __init__(self, name: str, path: str, icon_name: str):
        super().__init__()
        self._name = name
        self._path = path
        self._icon_name = icon_name

    @GObject.Property(type=str)
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @GObject.Property(type=str)
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    @GObject.Property(type=str)
    def icon_name(self):
        return self._icon_name

    @icon_name.setter
    def icon_name(self, value):
        self._icon_name = value


BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('file_column.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class FileColumnView(Gtk.Box):
    __gtype_name__ = 'FileColumnView'

    _column_view: Gtk.ColumnView = Gtk.Template.Child()

    def __init__(self, view_model: BlackFennecViewModel):
        super().__init__()
        self.model: Gtk.ListStore = self._create_file_column_model(None)
        self._view_model: BlackFennecViewModel = view_model

    def load_directory(self, directory_location: str):
        self.model.remove_all()
        self.model.append(
            FileEntry(
                os.path.basename(directory_location),
                directory_location,
                'folder-symbolic'
            )
        )
        tree_model = Gtk.TreeListModel.new(
            root=self.model,
            passthrough=False,
            autoexpand=False,
            create_func=self._create_file_column_model)
        self.selection = Gtk.SingleSelection(model=tree_model)
        self._column_view.set_model(self.selection)
        self._column_view.connect('activate', self._on_column_view_activated)

    @staticmethod
    def _create_file_column_model(item):
        model = Gio.ListStore(item_type=FileEntry)
        if item is None:
            return model
        else:
            if type(item) == Gtk.TreeListRow:
                item: FileEntry = item.get_item()

            if os.path.isdir(item.path):
                children = os.listdir(item.path)
                for child in children:
                    child_path = os.path.join(item.path, child)
                    child_icon = 'folder-symbolic' if os.path.isdir(child_path) \
                        else 'emblem-documents-symbolic'
                    model.append(
                        FileEntry(child, child_path, child_icon)
                    )
                return model
            else:
                return None

    def _on_column_view_activated(self, unused_sender, unused_row):
        selected_item = self.selection.get_selected_item()
        if selected_item is None:
            return
        selected_item: FileEntry = selected_item.get_item()
        if self._view_model.can_handle_uri(selected_item.path):
            self._view_model.open_file(selected_item.path)
        else:
            os.system(f'xdg-open {selected_item.path}')
