# -*- coding: utf-8 -*-
import logging
import os
import traceback
from pathlib import Path

from gi.repository import Adw, Gtk, Gio

from blackfennec.action_system.context import Context
from blackfennec.presentation_system.about_window.about_window_view import AboutWindowView
from blackfennec.presentation_system.main_window.document_tab import DocumentTab
from blackfennec.presentation_system.main_window.document_tab_view import DocumentTabView
from blackfennec.presentation_system.main_window.file_column_view import FileColumnView
from blackfennec.presentation_system.ui_service.message import Message
from blackfennec.presentation_system.ui_service.ui_service import UiService

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('black_fennec.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class BlackFennecView(Gtk.ApplicationWindow):
    __gtype_name__ = 'BlackFennecView'

    _file_tree_flap: Adw.Flap = Gtk.Template.Child()

    _toast_overlay: Adw.ToastOverlay = Gtk.Template.Child()
    _tab_overview: Gtk.Box = Gtk.Template.Child()
    _tab_view: Adw.TabView = Gtk.Template.Child()
    _tab_bar: Adw.TabBar = Gtk.Template.Child()

    _open_directory_button: Gtk.Button = Gtk.Template.Child()
    _open_file_button: Gtk.Button = Gtk.Template.Child()

    _empty_list_pattern: Adw.StatusPage = Gtk.Template.Child()

    def __init__(self, app, view_model, ui_service: UiService):
        super().__init__(application=app)
        self._application = app
        self._tab_menu_page = None
        self._file_chooser_native = None
        self._active_history = None

        self._view_model = view_model
        self._view_model.bind(
            open_file=self.on_open_tab,
            open_directory=self._update_directory,
        )

        self._ui_service = ui_service
        self._ui_service.register_message_overlay(self._toast_overlay)

        self.connect('destroy', self.on_close)

        self._init_main_actions()
        self._init_tabs()
        self._file_tree = FileColumnView(self._view_model)
        self._file_tree_flap.set_flap(self._file_tree)

        self._current_directory = None

    def on_close(self):
        self._ui_service.deregister_message_overlay(self._toast_overlay)

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
                    new_window = BlackFennecView(
                        self._application,
                        new_window_view_model,
                        self._ui_service,
                    )
                    new_window.present()
                    new_window_view_model.current_directory = directory_location
                    self._ui_service.show_message(
                        Context(self),
                        Message('New window opened')
                    )
                elif response == Gtk.ResponseType.ACCEPT.value_nick:
                    self._init_new_directory(directory_location)
                dialog.destroy()

            dialog.connect('response', on_response)
            dialog.present()

    def _init_new_directory(self, directory_location: str):
        if not directory_location:
            return
        self._current_directory = directory_location

        self._file_tree.load_directory(directory_location)
        if not self._file_tree_flap.get_reveal_flap():
            self._file_tree_flap.set_reveal_flap(True)

        self._ui_service.show_message(
            Context(self),
            Message(
                f'Directory opened: {os.path.basename(directory_location)}',
            )
        )

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
                self._ui_service.show_message(
                    Context(self),
                    Message(
                        'File selection canceled',
                    )
                )
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
        self._ui_service.show_message(
            Context(self),
            Message(f'Saved as: {current_page.document_tab.document.uri}'),
        )

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
                self._ui_service.show_message(
                    Context(self),
                    Message(f'Saved as: {file_path}')
                )
            else:
                logger.debug('Save as canceled')
                self._ui_service.show_message(
                    Context(self),
                    Message(f'Save as canceled')
                )
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
        self._ui_service.show_message(
            Context(self),
            Message(
                'All files saved',
            )
        )

    def on_go_to_store(self, unused_action, unused_param, unused_none) -> None:
        os.system('xdg-open /app/org.blackfennec.app.flatpakref')

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
        try:
            self._view_model.undo(current_page.document_tab)
            self._ui_service.show_message(
                Context(self),
                Message(
                    'Undo successful',
                    action_name='Redo',
                    action_target='main.redo',
                )
            )
        except ValueError:
            self._ui_service.show_message(
                Context(self),
                Message('Nothing to undo'),
            )
            logger.info('Nothing to undo')

    def on_redo(self, unused_action, unused_param, unused_data):
        current_page = self.get_current_page()
        try:
            self._view_model.redo(current_page.document_tab)
            self._ui_service.show_message(
                Context(self),
                Message(
                    'Redo successful',
                    action_name='Undo',
                    action_target='main.undo',
                )
            )
        except ValueError:
            self._ui_service.show_message(
                Context(self),
                Message('Cannot redo'),
            )
            logger.info('Nothing to undo')

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
        self._tab_view.connect('close-page', self.on_close_tab)
        self._tab_view.connect('create-window', self.on_create_new_window)
        self._tab_view.connect('setup-menu', self.on_setup_tab_menu)
        self._tab_view.connect('page-attached', self.on_attach_tab)

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
        self._toast_overlay.set_child(self._tab_overview)
        self.set_main_action_enabled('save', True)
        self.set_main_action_enabled('save_as', True)
        self.set_main_action_enabled('save_all', True)

    def hide_tab_view(self):
        if self._tab_view.get_n_pages() <= 1:
            self._toast_overlay.set_child(self._empty_list_pattern)
            self.set_main_action_enabled('save', False)
            self.set_main_action_enabled('save_as', False)
            self.set_main_action_enabled('save_all', False)

    def on_open_tab(self, unused_sender, tab: DocumentTab):
        document_tab_view = DocumentTabView(self._tab_view, tab)
        tab_page = document_tab_view.tab_page
        self._tab_view.set_selected_page(tab_page)
        self._ui_service.show_message(
            Context(self),
            Message(f'Opened file: {tab.title}')
        )

    def on_close_tab(self, action, page: Adw.TabPage):
        self._view_model.close_file(page.document_tab)
        self.hide_tab_view()
        self._ui_service.show_message(
            Context(self),
            Message(f'Closed file: {page.document_tab.title}')
        )

    def on_attach_tab(
            self,
            unused_tab_view: Adw.TabView,
            tab_page: Adw.TabPage,
            unused_position: int
    ):
        try:
            if hasattr(tab_page, 'document_tab'):
                self._view_model.attach_tab(tab_page.document_tab)
                self._ui_service.show_message(
                    Context(self),
                    Message(f'Tab attached')
                )
            self.show_tab_view()
        except AssertionError as e:
            message_text = \
                f'Tab already attached'
            self._ui_service.show_message(
                Context(self, tab_page.document_tab.document.content),
                Message(message_text)
            )
            logger.warning(message_text)
            logger.warning(traceback.format_exc())

    def on_detach_tab(
            self,
            unused_tab_view: Adw.TabView,
            tab_page: Adw.TabPage,
            unused_position: int
    ):
        try:
            self._view_model.detach_tab(tab_page.document_tab)
            self.hide_tab_view()
            self._ui_service.show_message(
                Context(self),
                Message(f'Tab detached: {tab_page.document_tab.title}')
            )
        except AssertionError as e:
            message_text = \
                f'Failed to detach tab: {tab_page.document_tab.title}'
            self._ui_service.show_message(
                Context(self),
                Message(str(e))
            )
            logger.warning(message_text)
            logger.warning(traceback.format_exc())

    def get_current_page(self):
        if self._tab_menu_page:
            return self._tab_menu_page
        else:
            return self._tab_view.get_selected_page()

    def on_create_new_window(self, tab_view: Adw.TabView):
        new_window_view_model = self._view_model.copy()
        new_window = BlackFennecView(
            self._application,
            new_window_view_model,
            self._ui_service)
        new_window.present()
        return new_window._tab_view

    def on_tab_move_to_new_window(
            self,
            unused_action,
            unused_param,
            unused_none
    ):
        new_window_view_model = self._view_model.copy()
        new_window = BlackFennecView(
            self._application,
            new_window_view_model,
            self._ui_service,
        )
        self._tab_view.transfer_page(
            self.get_current_page(),
            new_window._tab_view,
            0
        )
        new_window.present()

    def on_tab_pin(self, unused_action, unused_param, unused_none):
        self._tab_view.set_page_pinned(self.get_current_page(), True)

    def on_tab_unpin(self, unused_action, unused_param, unused_page):
        self._tab_view.set_page_pinned(self.get_current_page(), False)

    def on_tab_save(self, action, param, none):
        self.on_save(action, param, none)

    def on_tab_save_as(self, action, param, none):
        self.on_save_as(action, param, none)

    def on_tab_close_other(self, unused_action, unused_param, unused_page):
        self._tab_view.close_other_pages(self.get_current_page())

    def on_tab_close_before(self, unused_action, unused_param, unused_page):
        self._tab_view.close_pages_before(self.get_current_page())

    def on_tab_close_after(self, unused_action, unused_param, unused_page):
        self._tab_view.close_pages_after(self.get_current_page())

    def on_tab_close(self, unused_action, unused_param, unused_page):
        self._tab_view.close_page(self.get_current_page())

    def on_tab_close_all(self, unused_action, unused_param, unused_page):
        self._tab_view.close_other_pages(self.get_current_page())
        self._tab_view.close_page(self.get_current_page())
