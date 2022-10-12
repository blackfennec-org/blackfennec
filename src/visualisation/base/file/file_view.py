# -*- coding: utf-8 -*-
import logging
from pathlib import Path

from gi.repository import Gtk, Adw

from src.visualisation.base.file.file_view_model import FileViewModel

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('file_view.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class FileView(Adw.Bin):
    """View for the core type File."""

    __gtype_name__ = 'FileView'
    _file_path_value: Gtk.Label = Gtk.Template.Child()
    _file_type_value: Gtk.Label = Gtk.Template.Child()

    def __init__(self, view_model: FileViewModel):
        """Construct with view_model.

        Args:
            view_model (FileViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._set_file_path()
        self._set_file_type()
        logger.info(
            'FileView created'
        )

    def _set_file_path(self):
        file_path = self._view_model.file_path
        self._file_path_value.set_text(str(file_path))

    def _set_file_type(self):
        file_type = self._view_model.file_type
        self._file_type_value.set_text(str(file_type))

    @Gtk.Template.Callback()
    def on_choose_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        logger.debug('choose clicked')
        dialog = Gtk.FileChooserDialog(
            title='Please choose a file',
            action=Gtk.FileChooserAction.OPEN
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
            self._view_model.file_path = filename
            self._set_file_path()
        elif response == Gtk.ResponseType.CANCEL:
            logger.debug('file selection canceled')

        dialog.destroy()
