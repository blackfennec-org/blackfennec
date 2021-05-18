import logging
from gi.repository import Gtk
import os

from uri import URI

logger = logging.getLogger(__name__)


def create_folder_structure(root_directory):
    store = Gtk.TreeStore(str, str)
    s = dict()
    s[root_directory] = None
    for sub_directory, directories, files in os.walk(root_directory):
        for file in files:
            store.append(s[sub_directory], [file, sub_directory + '/' + file])
        for directory in directories:
            p = store.append(
                s[sub_directory],
                [directory, 'directory is not a file...']
            )
            s[sub_directory + '/' + directory] = p
    return store


@Gtk.Template(filename='src/visualisation/main_window/black_fennec.glade')
class BlackFennecView(Gtk.ApplicationWindow):
    """Black Fennec Main UI view"""
    __gtype_name__ = 'BlackFennecView'
    _presenter_container = Gtk.Template.Child()
    _file_tree = Gtk.Template.Child()
    _empty_list_pattern = Gtk.Template.Child()

    def __init__(self, app, view_model):
        super().__init__(application=app)
        logger.info('BlackFennecView __init__')
        self._view_model = view_model
        self._view_model.bind(tabs=self._update_tabs)
        self._tabs = set()

        renderer = Gtk.CellRendererText()
        tree_view_column = Gtk.TreeViewColumn(
            'Project', renderer, text=0)
        self._file_tree.append_column(tree_view_column)

    @Gtk.Template.Callback()
    def on_new_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        self._view_model.new()
        logger.debug('new clicked')

    @Gtk.Template.Callback()
    def on_open_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        logger.debug('open clicked')
        dialog = Gtk.FileChooserDialog(
            title='Please choose a project directory',
            parent=self,
            action=Gtk.FileChooserAction.SELECT_FOLDER
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,
            Gtk.ResponseType.OK,
        )

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            filename = dialog.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            logger.debug('Directory selection canceled')

        dialog.destroy()

        store = create_folder_structure(filename)
        self._file_tree.set_model(store)

    @Gtk.Template.Callback()
    def on_file_clicked(self, unused_sender, path, unused_column) -> None:
        model = self._file_tree.get_model()
        iterator = model.get_iter(path)
        if iterator:
            uri = URI(model.get_value(iterator, 1))
            self._view_model.open(uri)

    @Gtk.Template.Callback()
    def on_quit_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        self._view_model.quit()
        logger.debug('quit clicked')

    @Gtk.Template.Callback()
    def on_save_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        self._view_model.save()
        logger.debug('save clicked')

    @Gtk.Template.Callback()
    def on_save_as_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        self._view_model.save_as()
        logger.debug('save as clicked')

    @Gtk.Template.Callback()
    def on_go_to_store_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        self._view_model.go_to_store()
        logger.debug('go to store clicked')

    @Gtk.Template.Callback()
    def on_about_and_help_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        self._view_model.about_and_help()
        logger.debug('about and help clicked')

    @Gtk.Template.Callback()
    def on_close_tab_clicked(self, sender):
        self._view_model.close_tab(sender.get_name())

    def _update_tabs(self, unused_sender, tabs):
        if len(self._tabs) == 0:
            self._presenter_container.remove_page(0)
            self._show_tab()

        intersection = self._tabs.intersection(tabs)
        to_be_added = tabs.difference(intersection)
        for tab in to_be_added:
            notebook = self._presenter_container
            tab_box = self._create_tab_widget(tab)

            page_index = notebook.append_page_menu(tab.presenter, tab_box, Gtk.Label.new(tab.uri.path.name))
            notebook.set_tab_reorderable(self._presenter_container.get_nth_page(page_index), True)

        to_be_deleted = self._tabs.difference(intersection)
        for tab in to_be_deleted:
            index = self._presenter_container.page_num(tab.presenter)
            self._presenter_container.remove_page(index)

        self._tabs = set(tabs)
        if not self._tabs:
            self._add_empty_list_pattern()

        self._presenter_container.show_all()

    def _add_empty_list_pattern(self):
        self._presenter_container.append_page(
            self._empty_list_pattern,
            Gtk.Label.new(""))
        self._presenter_container.child_set_property(self._presenter_container.get_nth_page(0), 'tab-expand', True)
        self._hide_tab()

    def _hide_tab(self):
        style_context = self._presenter_container.get_style_context()
        style_context.add_class('hide-tab')

    def _show_tab(self):
        style_context = self._presenter_container.get_style_context()
        style_context.remove_class('hide-tab')

    def _create_tab_widget(self, tab):
        button_image = Gtk.Image.new()
        button_image.set_from_icon_name("application-exit", Gtk.IconSize.BUTTON)

        tab_button = Gtk.Button.new()
        tab_button.set_name(str(tab.uri))
        tab_button.set_image(button_image)
        tab_button.connect("clicked", self.on_close_tab_clicked)

        tab_box = Gtk.Box.new(0, 5)
        tab_box.pack_start(Gtk.Label.new(tab.uri.path.name), False, False, 0)
        tab_box.pack_end(tab_button, True, True, 0)
        tab_box.show_all()

        return tab_box
