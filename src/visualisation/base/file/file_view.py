# -*- coding: utf-8 -*-
import logging
from pathlib import Path

from gi.repository import Gtk, Adw

from src.visualisation.base.file.file_view_model import FileViewModel

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
        self._set_file_path(self._view_model.file_path)
        self._set_mime_type(self._view_model.file_type)

        logger.info('FileView created')

    def _set_file_path(self, file_path):
        self._view_model.file_path = file_path
        self._file_path.set_text(str(file_path))

    def _set_mime_type(self, file_type):
        self._view_model.file_type = file_type
        self._mime_type.set_text(str(file_type))

    @Gtk.Template.Callback()
    def _on_choose_file(self, unused_sender) -> None:
        """Callback for the button click event"""

        dialog = Gtk.FileChooserDialog(
            title='Please choose a file',
            action=Gtk.FileChooserAction.OPEN
        )

        dialog.add_buttons(
            'Cancel', Gtk.ResponseType.CANCEL,
            'Open', Gtk.ResponseType.OK
        )

        def on_response(dialog, response):
            if response == Gtk.ResponseType.OK:
                liststore = dialog.get_files()
                self._set_file_path(liststore[0].get_path())
            else:
                logger.debug('File selection canceled')
            dialog.destroy()

        dialog.connect('response', on_response)
        dialog.show()
