# -*- coding: utf-8 -*-
import logging
from pathlib import Path

from gi.repository import Gtk, Adw

from base.file.file_view_model import FileViewModel

from blackfennec.util.change_notification import ChangeNotification

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('file_view.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class FileView(Adw.PreferencesGroup):
    """View for the core type File."""

    __gtype_name__ = 'FileView'
    _file_path: Adw.EntryRow = Gtk.Template.Child()
    _mime_type: Adw.EntryRow = Gtk.Template.Child()

    def __init__(self, view_model: FileViewModel):
        """Construct with view_model.

        Args:
            view_model (FileViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._view_model.bind(changed=self._update_values)

        self._update_values()

        logger.info('FileView created')
        self._file_chooser_native = None

    def _update_values(self,
            unused_sender = None,
            unused_notification: ChangeNotification = None):
        self._file_path.set_text(self._view_model.file_path or 'empty path')
        self._mime_type.set_text(self._view_model.file_type or 'empty mime type')

    @Gtk.Template.Callback()
    def _on_choose_file(self, unused_sender) -> None:
        """Callback for the button click event"""

        dialog = Gtk.FileChooserNative(
            title='Choose file to open',
            transient_for=self.get_root(),
            action=Gtk.FileChooserAction.OPEN,
        )

        def on_response(dialog, response):
            if response == Gtk.ResponseType.ACCEPT:
                liststore = dialog.get_files()
                path = liststore[0].get_path()
                self._view_model.absolute_path = path
            else:
                logger.debug('File selection canceled')
            dialog.destroy()
            self._file_chooser_native = None

        dialog.connect('response', on_response)
        dialog.show()
        self._file_chooser_native = dialog
