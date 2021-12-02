# -*- coding: utf-8 -*-
import logging

from gi.repository import Gtk

from src.visualisation.base.file.file_view_model import FileViewModel

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/visualisation/base/file/file_preview.glade')
class FilePreview(Gtk.Bin):
    """Preview for the core type File."""

    __gtype_name__ = 'FilePreview'
    _file_path_value: Gtk.Label = Gtk.Template.Child()

    def __init__(self, view_model: FileViewModel):
        """Construct with view_model.

        Args:
            view_model (FileViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._set_file_path()
        logger.info(
            'FileView created'
        )

    def _set_file_path(self):
        file_path = self._view_model.file_path
        self._file_path_value.set_text(str(file_path))

    @Gtk.Template.Callback()
    def _preview_clicked(self, unused_sender, unused_argument) -> None:
        """Handles clicks on file items, triggers navigation"""
        self._view_model.navigate()
