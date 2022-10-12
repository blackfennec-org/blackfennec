# -*- coding: utf-8 -*-
import logging
import os
from pathlib import Path

from gi.repository import Adw, Gtk

from src.black_fennec.facade.extension_store.extension_store_view import ExtensionStoreView
from src.black_fennec.facade.main_window.document_tab import DocumentTab
from src.black_fennec.facade.main_window.document_tab_view import DocumentTabView

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('black_fennec.ui'))


def create_folder_structure(root_directory):
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


@Gtk.Template(filename=UI_TEMPLATE)
class BlackFennecView(Gtk.ApplicationWindow):
    __gtype_name__ = 'BlackFennecView'

    _file_tree: Gtk.TreeView = Gtk.Template.Child()
    _file_tree_flap: Adw.Flap = Gtk.Template.Child()

    _tab_overview: Gtk.Box = Gtk.Template.Child()
    _tab_view: Adw.TabView = Gtk.Template.Child()
    _tab_bar: Adw.TabBar = Gtk.Template.Child()

    def __init__(self, app, view_model):
        self._application = app
        app.create_action('main.quit', self.on_quit_clicked, ['<primary>q'])
        app.create_action('main.settings', self.on_settings_action)
        app.create_action('main.open', self.on_open_clicked)
        app.create_action('main.save', self.on_save_clicked)
        app.create_action('main.save_as', self.on_save_as_clicked)
        app.create_action('main.extension_store', self.on_go_to_store_clicked)
        app.create_action('main.about', self.on_about_clicked)

        super().__init__(application=app)
        logger.info('BlackFennecView __init__')
        self._view_model = view_model
        self._view_model.bind(create_tab=self._create_tab)
        self._view_model.bind(project=self._update_project)
        self._tabs = set()

        renderer = Gtk.CellRendererText()
        tree_view_column = Gtk.TreeViewColumn(
            'Project', renderer, text=0)
        self._file_tree.append_column(tree_view_column)

    @Gtk.Template.Callback()
    def on_flap_button_toggled(self, toggle_button):
        self._file_tree_flap.set_reveal_flap(not self._file_tree_flap.get_reveal_flap())

    @Gtk.Template.Callback()
    def on_file_clicked(self, unused_sender, path, unused_column) -> None:
        model = self._file_tree.get_model()
        iterator = model.get_iter(path)
        if iterator:
            uri = model.get_value(iterator, 1)
            self._view_model.open_file(uri)

    def _update_project(self, unused_sender, project_location: str):
        store = create_folder_structure(project_location)
        self._file_tree.set_model(store)
        if not self._file_tree_flap.get_reveal_flap():
            self._file_tree_flap.set_reveal_flap(True)

    def _create_tab(self, unused_sender, tab: DocumentTab):
        DocumentTabView(self._tab_view, tab)

    def on_open_clicked(self, action, param) -> None:
        """Callback for the button click event"""
        logger.debug('open clicked')
        dialog = Gtk.FileChooserDialog(
            title='Please choose a project directory',
            transient_for=self,
            action=Gtk.FileChooserAction.SELECT_FOLDER
        )
        dialog.add_buttons(
            'Cancel', Gtk.ResponseType.CANCEL,
            'Open', Gtk.ResponseType.OK
        )

        def on_response(dialog, response):
            if response == Gtk.ResponseType.OK:
                liststore = dialog.get_files()
                self._view_model.set_project(liststore[0].get_path())
            else:
                logger.debug('Directory selection canceled')
            dialog.destroy()

        dialog.connect('response', on_response)
        dialog.show()

    def on_save_clicked(self, action, param) -> None:
        """Callback for the button click event"""
        self._view_model.save()
        logger.debug('save clicked')

    def on_save_as_clicked(self, action, param) -> None:
        """Callback for the button click event"""
        self._view_model.save_as()
        logger.debug('save as clicked')

    def on_go_to_store_clicked(self, action, param) -> None:
        """Callback for the button click event"""
        store_view_model = self._view_model.create_extension_store()
        store = ExtensionStoreView(self._application, store_view_model)
        store.show()
        logger.debug('go to store clicked')

    def on_about_clicked(self, action, param) -> None:
        """Callback for the button click event"""
        self._view_model.about_and_help()
        logger.debug('About clicked')

    def on_close_tab_clicked(self, sender):
        self._view_model.close_tab(sender.get_name())

    def _add_empty_list_pattern(self):
        self._presenter_container.append_page(
            self._empty_list_pattern,
            Gtk.Label.new(''))
        self._presenter_container.child_set_property(
            self._presenter_container.get_nth_page(0), 'tab-expand', True)
        self._hide_tab()

    def on_quit_clicked(self, action, param):
        self._application.quit()

    def on_settings_action(self, action, param):
        logger.debug('settings clicked')
