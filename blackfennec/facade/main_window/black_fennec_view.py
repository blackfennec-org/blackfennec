# -*- coding: utf-8 -*-
import logging
import os
from pathlib import Path

from gi.repository import Adw, Gtk, Gio, GLib

from blackfennec.facade.about_window.about_window_view import AboutWindowView
from blackfennec.facade.extension_store.extension_store_view import \
    ExtensionStoreView
from blackfennec.facade.main_window.document_tab import DocumentTab
from blackfennec.facade.main_window.document_tab_view import DocumentTabView

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('black_fennec.ui'))


def create_directory_structure(root_directory):
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
    tab_view: Adw.TabView = Gtk.Template.Child()
    _tab_bar: Adw.TabBar = Gtk.Template.Child()

    _open_directory_button: Gtk.Button = Gtk.Template.Child()
    _open_file_button: Gtk.Button = Gtk.Template.Child()

    _empty_list_pattern: Adw.StatusPage = Gtk.Template.Child()

    def __init__(self, app, view_model, current_directory: str = None):
        super().__init__(application=app)

        self._application = app
        self._init_main_actions()

        self._tab_menu_page = None
        self._init_tabs()

        logger.info('BlackFennecView __init__')
        self._view_model = view_model
        self._view_model.bind(
            open_file=self.on_open_tab,
            open_directory=self._update_directory,
        )

        renderer = Gtk.CellRendererText()
        tree_view_column = Gtk.TreeViewColumn(
            'Current directory', renderer, text=0)
        self._file_tree.append_column(tree_view_column)

        self._current_directory = current_directory
        self._update_directory(self, self._current_directory)
        self._file_chooser_native = None

        self._active_history = None

    def _init_main_actions(self):
        self._main_action_group = Gio.SimpleActionGroup().new()
        self._main_action_group.add_action_entries([
            ('open_directory', self.on_open_directory),
            ('open_file', self.on_open_file),
            ('save', self.on_save),
            ('save_as', self.on_save_as),
            ('save_all', self.on_save_all),
            ('extension_store', self.on_go_to_store),
            ('about', self.on_about),
            ('quit', self.on_quit),
            ('undo', self.on_undo),
            ('redo', self.on_redo),
        ])

        self.insert_action_group('main', self._main_action_group)

        self._application.set_accels_for_action('main.open_directory',
                                                ['<primary><alt>o'])
        self._application.set_accels_for_action('main.open_file',
                                                ['<primary>o'])
        self._application.set_accels_for_action('main.save', ['<primary>s'])
        self._application.set_accels_for_action('main.save_as',
                                                ['<primary><shift>s'])
        self._application.set_accels_for_action('main.save_all',
                                                ['<primary><alt>s'])
        self._application.set_accels_for_action('main.extension_store',
                                                ['<primary>e'])
        self._application.set_accels_for_action('main.about', ['<primary>i'])
        self._application.set_accels_for_action('main.quit', ['<primary>q'])
        self._application.set_accels_for_action('main.undo', ['<primary>z'])
        self._application.set_accels_for_action('main.redo',
                                                ['<primary><shift>z'])

        self.set_main_action_enabled('save', False)
        self.set_main_action_enabled('save_as', False)
        self.set_main_action_enabled('save_all', False)

    def set_main_action_enabled(self, action_name: str, enabled: bool):
        action = self._main_action_group.lookup_action(action_name)
        action.set_enabled(enabled)

    @Gtk.Template.Callback()
    def on_flap_button_toggled(self, toggle_button):
        self._file_tree_flap.set_reveal_flap(
            not self._file_tree_flap.get_reveal_flap())

    def on_open_directory(self, unused_action, unused_param,
                          unused_none) -> None:
        """Callback for the button click event"""
        logger.debug('open clicked')
        dialog = Gtk.FileChooserNative(
            title='Choose directory',
            transient_for=self,
            action=Gtk.FileChooserAction.SELECT_FOLDER,
        )

        def on_response(dialog, response):
            if response == Gtk.ResponseType.ACCEPT:
                directory = dialog.get_file()
                file_path = directory.get_path()
                logger.info(f'Chosen file: {file_path}')
                self._view_model.current_directory = file_path
            else:
                logger.debug('Directory selection canceled')
            dialog.destroy()
            self._file_chooser_native = None

        dialog.connect('response', on_response)
        self._file_chooser_native = dialog
        dialog.show()
        self._update_opening_suggestions()

    def _update_opening_suggestions(self):
        open_dir_style = self._open_directory_button.get_style_context()
        open_file_style = self._open_file_button.get_style_context()
        open_dir_style.remove_class('suggested-action')
        open_file_style.add_class('suggested-action')

    def _update_directory(self, unused_sender, directory_location: str):
        if not self._current_directory:
            self._init_new_directory(directory_location)
        else:
            dialog = Adw.MessageDialog(
                transient_for=self,
                heading='Opening new directory',
                body='Where do you want to open the new directory?',
            )
            dialog.add_response(Gtk.ResponseType.CANCEL.value_nick, 'Cancel')
            dialog.add_response('open_in_new', 'New window')
            dialog.add_response(Gtk.ResponseType.ACCEPT.value_nick,
                                'This window')

            dialog.set_response_appearance(Gtk.ResponseType.ACCEPT.value_nick,
                                           Adw.ResponseAppearance.DESTRUCTIVE)
            dialog.set_response_appearance('open_in_new',
                                           Adw.ResponseAppearance.SUGGESTED)

            def on_response(dialog, response):
                if response == 'open_in_new':
                    new_window_view_model = self._view_model.copy()
                    new_window = BlackFennecView(self._application,
                                                 new_window_view_model)
                    new_window.present()
                    new_window_view_model.current_directory = directory_location
                elif response == Gtk.ResponseType.ACCEPT.value_nick:
                    self._init_new_directory(directory_location)
                dialog.destroy()

            dialog.connect('response', on_response)
            dialog.present()

    def _init_new_directory(self, directory_location: str):
        if not directory_location:
            return
        self._current_directory = directory_location

        store = create_directory_structure(directory_location)
        self._file_tree.set_model(store)
        if not self._file_tree_flap.get_reveal_flap():
            self._file_tree_flap.set_reveal_flap(True)

    @Gtk.Template.Callback()
    def on_open_file_from_filetree(self, unused_sender, path,
                                   unused_column) -> None:
        model = self._file_tree.get_model()
        iterator = model.get_iter(path)
        if iterator:
            uri = model.get_value(iterator, 1)
            self._view_model.open_file(uri)

    def on_open_file(self, unused_action, unused_param, unused_none) -> None:
        dialog = Gtk.FileChooserNative(
            title='Choose file to open',
            transient_for=self,
            action=Gtk.FileChooserAction.OPEN,
        )
        if self._current_directory:
            dialog.set_current_folder(
                Gio.File.new_for_path(self._current_directory))

        def on_response(dialog, response):
            if response == Gtk.ResponseType.ACCEPT:
                files = dialog.get_files()
                for file in files:
                    logger.info(f'Chosen file: {file}')
                    self._view_model.open_file(file.get_path())
            else:
                logger.debug('File selection canceled')
            dialog.destroy()
            self._file_chooser_native = None

        dialog.connect('response', on_response)
        self._file_chooser_native = dialog
        dialog.show()

    def on_save(self, unused_action, unused_param, unused_none) -> None:
        """Callback for the button click event"""
        current_page = self.get_current_page()
        self._view_model.save(current_page.document_tab)
        logger.debug('save clicked')

    def on_save_as(self, unused_action, unused_param, unused_none) -> None:
        """Callback for the button click event"""
        current_page = self.get_current_page()
        dialog = Gtk.FileChooserNative(
            title='Choose directory',
            transient_for=self,
            action=Gtk.FileChooserAction.SAVE,
        )

        def on_response(dialog, response):
            if response == Gtk.ResponseType.ACCEPT:
                directory = dialog.get_file()
                file_path = directory.get_path()
                self._view_model.save_as(current_page.document_tab, file_path)
            else:
                logger.debug('Save as canceled')
            dialog.destroy()
            self._file_chooser_native = None

        dialog.connect('response', on_response)
        self._file_chooser_native = dialog
        dialog.show()
        logger.debug('save as clicked')

    def on_save_all(self, unused_action, unused_param, unused_none) -> None:
        """Callback for the button click event"""
        self._view_model.save_all()
        logger.debug('save all clicked')

    def on_go_to_store(self, unused_action, unused_param, unused_none) -> None:
        """Callback for the button click event"""
        store_view_model = self._view_model.create_extension_store()
        store = ExtensionStoreView(self._application, store_view_model)
        store.show()
        logger.debug('go to store clicked')

    def on_about(self, unused_action, unused_param, unused_none) -> None:
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

    def on_quit(self, unused_action, unused_param, unused_none):
        self.close()

    def on_settings_action(self, unused_action, unused_param, unused_none):
        logger.debug('settings clicked')

    def on_undo(self, unused_action, unused_param, unused_data):
        current_page = self.get_current_page()
        tab = current_page.document_tab
        if tab.history.can_undo():
            tab.history.undo()
        else:
            logger.warning('Cannot undo')

    def on_redo(self, unused_action, unused_param, unused_data):
        current_page = self.get_current_page()
        tab = current_page.document_tab
        if tab.history.can_redo():
            tab.history.redo()
        else:
            logger.warning('Cannot redo')

    """Tab handling"""

    def _init_tabs(self):
        self._tab_action_group = Gio.SimpleActionGroup().new()
        self._tab_action_group.add_action_entries([
            ('move_to_new_window', self.on_tab_move_to_new_window),
            ('pin', self.on_tab_pin),
            ('unpin', self.on_tab_unpin),
            ('save', self.on_tab_save),
            ('save_as', self.on_tab_save_as),
            ('close_other', self.on_tab_close_other),
            ('close_before', self.on_tab_close_before),
            ('close_after', self.on_tab_close_after),
            ('close', self.on_tab_close),
            ('close_all', self.on_tab_close_all),
        ])

        self.insert_action_group('tab', self._tab_action_group)
        self.tab_view.connect('close-page', self.on_close_tab)
        self.tab_view.connect('create-window', self.on_create_new_window)
        self.tab_view.connect('setup-menu', self.on_setup_tab_menu)
        self.tab_view.connect('page-attached', self.on_attach_tab)

    def on_setup_tab_menu(self, view: Adw.TabView, page: Adw.TabPage):
        prev: Adw.TabPage = None
        can_close_before = True
        can_close_after = True
        pinned = False

        self._tab_menu_page = page

        n_pages = view.get_n_pages()

        if page:
            pos = view.get_page_position(page)

            if pos > 0:
                prev = view.get_nth_page(pos - 1)

            pinned = page.get_pinned()
            prev_pinned = prev and prev.get_pinned()

            can_close_before = not pinned and prev and not prev_pinned
            can_close_after = pos < n_pages - 1

        self.set_tab_action_enabled("pin", not page or not pinned)
        self.set_tab_action_enabled("unpin", not page or pinned)
        self.set_tab_action_enabled("close", not page or not pinned)
        self.set_tab_action_enabled("close_all",
                                    not page or (not pinned and n_pages > 1))
        self.set_tab_action_enabled("close_before", can_close_before)
        self.set_tab_action_enabled("close_after", can_close_after)
        self.set_tab_action_enabled("close_other",
                                    can_close_before or can_close_after)
        self.set_tab_action_enabled("move_to_new_window",
                                    not page or (not pinned and n_pages > 1))

    def set_tab_action_enabled(self, action_name: str, enabled: bool):
        action = self._tab_action_group.lookup_action(action_name)
        action.set_enabled(enabled)

    def show_tab_view(self):
        self._file_tree_flap.set_content(self._tab_overview)
        self.set_main_action_enabled('save', True)
        self.set_main_action_enabled('save_as', True)
        self.set_main_action_enabled('save_all', True)

    def hide_tab_view(self):
        if self.tab_view.get_n_pages() <= 1:
            self._file_tree_flap.set_content(self._empty_list_pattern)
            self.set_main_action_enabled('save', False)
            self.set_main_action_enabled('save_as', False)
            self.set_main_action_enabled('save_all', False)

    def on_open_tab(self, unused_sender, tab: DocumentTab):
        document_tab_view = DocumentTabView(self.tab_view, tab)
        tab_page = document_tab_view.tab_page
        self.tab_view.set_selected_page(tab_page)

    def on_close_tab(self, action, page: Adw.TabPage):
        self._view_model.close_file(page.document_tab)
        self.hide_tab_view()

    def on_attach_tab(
            self,
            unused_tab_view: Adw.TabView,
            tab_page: Adw.TabPage,
            unused_position: int
    ):
        if hasattr(tab_page, 'document_tab'):
            self._view_model.attach_tab(tab_page.document_tab)
        self.show_tab_view()

    def on_detach_tab(
            self,
            unused_tab_view: Adw.TabView,
            tab_page: Adw.TabPage,
            unused_position: int
    ):
        self._view_model.detach_tab(tab_page.document_tab)
        self.hide_tab_view()

    def get_current_page(self):
        if self._tab_menu_page:
            return self._tab_menu_page
        else:
            return self.tab_view.get_selected_page()

    def on_create_new_window(self, tab_view: Adw.TabView):
        new_window_view_model = self._view_model.copy()
        new_window = BlackFennecView(self._application, new_window_view_model)
        new_window.present()
        return new_window.tab_view

    def on_tab_move_to_new_window(
            self,
            unused_action,
            unused_param,
            unused_none
    ):
        new_window_view_model = self._view_model.copy()
        new_window = BlackFennecView(self._application, new_window_view_model)
        self.tab_view.transfer_page(
            self.get_current_page(),
            new_window.tab_view,
            0
        )
        new_window.present()

    def on_tab_pin(self, unused_action, unused_param, unused_none):
        self.tab_view.set_page_pinned(self.get_current_page(), True)

    def on_tab_unpin(self, unused_action, unused_param, unused_page):
        self.tab_view.set_page_pinned(self.get_current_page(), False)

    def on_tab_save(self, action, param, none):
        self.on_save(action, param, none)

    def on_tab_save_as(self, action, param, none):
        self.on_save_as(action, param, none)

    def on_tab_close_other(self, unused_action, unused_param, unused_page):
        self.tab_view.close_other_pages(self.get_current_page())

    def on_tab_close_before(self, unused_action, unused_param, unused_page):
        self.tab_view.close_pages_before(self.get_current_page())

    def on_tab_close_after(self, unused_action, unused_param, unused_page):
        self.tab_view.close_pages_after(self.get_current_page())

    def on_tab_close(self, unused_action, unused_param, unused_page):
        self.tab_view.close_page(self.get_current_page())

    def on_tab_close_all(self, unused_action, unused_param, unused_page):
        self.tab_view.close_other_pages(self.get_current_page())
        self.tab_view.close_page(self.get_current_page())
