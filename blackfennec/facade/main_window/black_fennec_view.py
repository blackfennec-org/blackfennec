# -*- coding: utf-8 -*-
import logging
import os
from pathlib import Path

from gi.repository import Adw, Gtk, Gio

from blackfennec.facade.about_window.about_window_view import AboutWindowView
from blackfennec.facade.extension_store.extension_store_view import ExtensionStoreView
from blackfennec.facade.main_window.document_tab import DocumentTab
from blackfennec.facade.main_window.document_tab_view import DocumentTabView

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

    _open_project_button: Gtk.Button = Gtk.Template.Child()
    _open_file_button: Gtk.Button = Gtk.Template.Child()

    _empty_list_pattern: Adw.StatusPage = Gtk.Template.Child()

    def __init__(self, app, view_model, current_project: str = None):
        self._application = app
        app.create_action('main.quit', self.on_quit_clicked, ['<primary>q'])
        app.create_action('main.settings', self.on_settings_action)
        app.create_action('main.open_project', self.on_open_project)
        app.create_action('main.open_file', self.on_open_file)
        app.create_action('main.save', self.on_save_clicked)
        app.create_action('main.save_as', self.on_save_as_clicked)
        app.create_action('main.extension_store', self.on_go_to_store_clicked)
        app.create_action('main.about', self.on_about_clicked)

        super().__init__(application=app)
        logger.info('BlackFennecView __init__')
        self._view_model = view_model
        self._view_model.bind(
            open_file=self.on_open_tab,
            project=self._update_project,
        )

        self._tab_view.connect('close-page', self.on_close_tab)
        self.tabs = {}

        renderer = Gtk.CellRendererText()
        tree_view_column = Gtk.TreeViewColumn(
            'Project', renderer, text=0)
        self._file_tree.append_column(tree_view_column)

        self._current_project = current_project
        self._update_project(self, self._current_project)
        self._file_chooser_native = None

    @Gtk.Template.Callback()
    def on_flap_button_toggled(self, toggle_button):
        self._file_tree_flap.set_reveal_flap(not self._file_tree_flap.get_reveal_flap())

    def on_open_project(self, action, param) -> None:
        """Callback for the button click event"""
        logger.debug('open clicked')
        dialog = Gtk.FileChooserNative(
            title='Choose project directory',
            transient_for=self,
            action=Gtk.FileChooserAction.SELECT_FOLDER,
        )

        def on_response(dialog, response):
            if response == Gtk.ResponseType.ACCEPT:
                folder = dialog.get_file()
                file_path = folder.get_path()
                self._view_model.set_project(file_path)
            else:
                logger.debug('Directory selection canceled')
            dialog.destroy()
            self._file_chooser_native = None

        dialog.connect('response', on_response)
        self._file_chooser_native = dialog
        dialog.show()

    def _update_project(self, unused_sender, project_location: str):
        if not self._current_project:
            self._init_new_project(project_location)
        else:
            dialog = Adw.MessageDialog(
                transient_for=self,
                heading='Opening new project',
                body='Where do you want to open the new project?',
            )
            dialog.add_response(Gtk.ResponseType.CANCEL.value_nick, 'Cancel')
            dialog.add_response('open_in_new', 'New window')
            dialog.add_response(Gtk.ResponseType.ACCEPT.value_nick, 'This window')

            dialog.set_response_appearance(Gtk.ResponseType.ACCEPT.value_nick, Adw.ResponseAppearance.DESTRUCTIVE)
            dialog.set_response_appearance('open_in_new', Adw.ResponseAppearance.SUGGESTED)

            def on_response(dialog, response):
                if response == 'open_in_new':
                    message = 'Opening in new window is not implemented yet'
                    logger.warning(message)
                    raise NotImplementedError(message)
                elif response == Gtk.ResponseType.ACCEPT.value_nick:
                    self._init_new_project(project_location)
                dialog.destroy()

            dialog.connect('response', on_response)
            dialog.present()

    def _init_new_project(self, project_location: str):
        if not project_location:
            return
        self._current_project = project_location

        store = create_folder_structure(project_location)
        self._file_tree.set_model(store)
        if not self._file_tree_flap.get_reveal_flap():
            self._file_tree_flap.set_reveal_flap(True)

    @Gtk.Template.Callback()
    def on_open_file_from_filetree(self, unused_sender, path, unused_column) -> None:
        model = self._file_tree.get_model()
        iterator = model.get_iter(path)
        if iterator:
            uri = model.get_value(iterator, 1)
            self._view_model.open_file(uri)

    def on_open_file(self, action, param) -> None:
        dialog = Gtk.FileChooserNative(
            title='Choose file to open',
            transient_for=self,
            action=Gtk.FileChooserAction.OPEN,
        )
        if self._current_project:
            dialog.set_current_folder(Gio.File.new_for_path(self._current_project))

        def on_response(dialog, response):
            if response == Gtk.ResponseType.ACCEPT:
                files = dialog.get_files()
                for file in files:
                    self._view_model.open_file(file.get_path())
            else:
                logger.debug('File selection canceled')
            dialog.destroy()
            self._file_chooser_native = None

        dialog.connect('response', on_response)
        self._file_chooser_native = dialog
        dialog.show()

    def on_open_tab(self, unused_sender, tab: DocumentTab):
        self._file_tree_flap.set_content(self._tab_overview)
        document_tab_view = DocumentTabView(self._tab_view, tab)
        tab_page = document_tab_view.tab_page
        self.tabs[tab_page] = tab
        self._tab_view.set_selected_page(tab_page)

    def on_close_tab(self, action, page):
        self._view_model.close_file(self.tabs[page])
        if self._tab_view.get_n_pages() <= 1:
            self._file_tree_flap.set_content(self._empty_list_pattern)

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
        about_view_model = self._view_model.get_about_window_view_model()
        about_window = AboutWindowView(about_view_model, self)
        about_window.adw_about_window.present()

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
