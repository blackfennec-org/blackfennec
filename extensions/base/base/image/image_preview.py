# -*- coding: utf-8 -*-
import logging
from pathlib import Path

from gi.repository import Gtk, Adw, Gdk

from base.image.image_view_model import ImageViewModel

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('image_preview.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class ImagePreview(Gtk.Button):
    """Preview for the core type Image."""

    __gtype_name__ = 'ImagePreview'
    _image: Gtk.Image = Gtk.Template.Child()

    def __init__(self, view_model: ImageViewModel):
        """Construct with view_model.

        Args:
            view_model (ImageViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._set_file_path(self._view_model.file_path)
        self._image.set_size(64)
        logger.info('ImageView created')

    def _set_image_from_path(self, file_path) -> None:
        try:
            paintable = Gdk.Texture.new_from_filename(file_path)
            self._set_image(paintable)
        except Exception as e:
            logger.warning(e)

    def _set_image(self, paintable) -> None:
        self._image.set_custom_image(paintable)

    def _set_file_path(self, file_path):
        self._view_model.file_path = file_path
        self._set_image_from_path(file_path)

    @Gtk.Template.Callback()
    def _on_navigate(self, unused_sender) -> None:
        """Handles clicks on image items, triggers navigation"""
        self._view_model.navigate()
