# -*- coding: utf-8 -*-
import logging
from pathlib import Path

from gi.repository import Gtk, Adw, GdkPixbuf

from src.visualisation.base.image.image_view_model import ImageViewModel

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('image_preview.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class ImagePreview(Adw.Bin):
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

        logger.info('ImageView created')

    def _set_image_from_path(self, file_path) -> None:
        try:
            pixbuf = self._get_pixbuf(file_path)
            pixbuf = self._rescale_pixbuf(pixbuf, 100)
            self._set_image(pixbuf)
        except Exception as e:
            logger.warning(e)
            self._set_file_not_found()

    def _get_pixbuf(self, file_path) -> GdkPixbuf.Pixbuf:
        return GdkPixbuf.Pixbuf.new_from_file(file_path)

    def _rescale_pixbuf(self, pixbuf, width) -> GdkPixbuf.Pixbuf:
        scaling = self._calculate_new_image_size_factor(width, pixbuf)
        old_width = pixbuf.get_width()
        old_height = pixbuf.get_height()
        pixbuf = pixbuf.scale_simple(
            old_width * scaling, old_height * scaling, 2)
        return pixbuf

    def _calculate_new_image_size_factor(self, width, pixbuf) -> float:
        old_width = pixbuf.get_width()
        factor = width / old_width
        return factor

    def _set_image(self, pixbuf) -> None:
        self._image.set_from_pixbuf(pixbuf)

    def _set_file_path(self, file_path):
        self._view_model.file_path = file_path
        self._set_image_from_path(file_path)

    def _set_file_not_found(self):
        self._image.set_from_file(str(BASE_DIR.joinpath('not-found.png')))

    @Gtk.Template.Callback()
    def _on_resize(self, unused_sender, unused_event) -> None:
        file_path = self._view_model.file_path
        pixbuf = self._get_pixbuf(file_path)
        width = self.get_allocation().width
        scaled_pixbuf = self._rescale_pixbuf(pixbuf, width - 50)
        self._set_image(scaled_pixbuf)

    @Gtk.Template.Callback()
    def _preview_clicked(self, unused_sender) -> None:
        """Handles clicks on image items, triggers navigation"""
        self._view_model.navigate()
