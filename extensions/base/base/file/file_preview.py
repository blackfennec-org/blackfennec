# -*- coding: utf-8 -*-
import logging
from pathlib import Path

from gi.repository import Gtk, Adw

from base.file.file_view_model import FileViewModel

from blackfennec.util.change_notification import ChangeNotification

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('file_preview.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class FilePreview(Gtk.Button):
    """Preview for the core type File."""

    __gtype_name__ = 'FilePreview'

    def __init__(self, view_model: FileViewModel):
        """Construct with view_model.

        Args:
            view_model (FileViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._view_model.bind(changed=self._set_file_path)

        self._set_file_path(self, ChangeNotification('', self._view_model.file_path))
        logger.info(
            'FileView created'
        )

    def _set_file_path(self, unused_sender, unused_notification: ChangeNotification):
        file_path = self._view_model.file_path or "empty path"
        self.set_tooltip_text(file_path or 'empty path')

    @Gtk.Template.Callback()
    def _on_navigate(self, unused_sender) -> None:
        """Handles clicks on file items, triggers navigation"""
        self._view_model.navigate()
