# -*- coding: utf-8 -*-
import logging
from pathlib import Path

from gi.repository import Gtk, Adw, Gdk

from base.image.image_view_model import ImageViewModel

from blackfennec.util.change_notification import ChangeNotification

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('image_preview.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class ImagePreview(Gtk.Button):
    """Preview for the core type Image."""

    __gtype_name__ = 'ImagePreview'
    _image: Adw.Avatar = Gtk.Template.Child()

    def __init__(self, view_model: ImageViewModel):
        """Construct with view_model.

        Args:
            view_model (ImageViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._view_model.bind(changed=self._update_values)

        self._update_values()

        self._image.set_size(64)

    def _set_image_from_path(self, file_path) -> None:
        try:
            paintable = Gdk.Texture.new_from_filename(file_path)
            self._image.set_custom_image(paintable)
        except Exception as e:
            self._set_image_not_found()
            logger.info(e)

    def _set_image_not_found(self):
        self._image.set_custom_image(None)

    def _update_values(self, 
            unused_sender=None,
            unused_notification: ChangeNotification = None):
        self._set_image_from_path(
            self._view_model.absolute_path)

    @Gtk.Template.Callback()
    def _on_navigate(self, unused_sender) -> None:
        """Handles clicks on image items, triggers navigation"""
        self._view_model.navigate()
