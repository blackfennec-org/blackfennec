import logging
from gi.repository import Gtk
import os

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

    def __init__(self, app, view_model):
        super().__init__(application=app)
        logger.info('BlackFennecView __init__')
        self._view_model = view_model
        self._presenter_container.add(self._view_model.presenter)
        self._presenter_container.show_all()

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
        renderer = Gtk.CellRendererText()
        tree_view_column = Gtk.TreeViewColumn(
            'Project', renderer, text=0)
        self._file_tree.append_column(tree_view_column)

    @Gtk.Template.Callback()
    def on_file_clicked(self, unused_sender, path, unused_column) -> None:
        model = self._file_tree.get_model()
        iterator = model.get_iter(path)
        if iterator:
            file = model.get_value(iterator, 1)
            self._view_model.open(file)

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
