# -*- coding: utf-8 -*-
import logging
from pathlib import Path

from gi.overrides.GObject import GObject
from gi.overrides.Gdk import Gdk
from gi.repository import Gtk, Adw

from src.visualisation.base.image.image_view_model import ImageViewModel

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('image_view.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class ImageView(Adw.PreferencesGroup):
    """View for the core type Image."""

    __gtype_name__ = 'ImageView'
    _file_path: Adw.EntryRow = Gtk.Template.Child()
    _mime_type: Adw.EntryRow = Gtk.Template.Child()
    _image: Gtk.Image = Gtk.Template.Child()

    def __init__(self, view_model: ImageViewModel):
        """Construct with view_model.

        Args:
            view_model (ImageViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._set_file_path(self._view_model.file_path)
        self._set_mime_type(self._view_model.file_type)

        logger.info('ImageView created')

    def _set_image_from_path(self, file_path) -> None:
        try:
            paintable = Gdk.Texture.new_from_filename(file_path)
            self._set_image(paintable)
        except Exception as e:
            logger.warning(e)

    def _set_image(self, paintable) -> None:
        self._image.set_from_paintable(paintable)

    def _set_file_path(self, file_path):
        self._view_model.file_path = file_path
        self._file_path.set_text(str(file_path))
        self._set_image_from_path(file_path)

    def _set_mime_type(self, file_type):
        self._view_model.file_type = file_type
        self._mime_type.set_text(str(file_type))

    def _set_file_not_found(self):
        self._image.set_from_icon_name('image-missing-symbolic', 64)

    @Gtk.Template.Callback()
    def _on_choose_image(self, unused_sender) -> None:
        """Callback for the button click event"""

        dialog = Gtk.FileChooserDialog(
            title='Please choose a image',
            action=Gtk.FileChooserAction.OPEN
        )

        filter = Gtk.FileFilter(name='Images')
        filter.add_pixbuf_formats()
        dialog.set_filter(filter)

        dialog.add_buttons(
            'Cancel', Gtk.ResponseType.CANCEL,
            'Open', Gtk.ResponseType.OK
        )

        def on_response(dialog, response):
            if response == Gtk.ResponseType.OK:
                liststore = dialog.get_files()
                self._set_file_path(liststore[0].get_path())
            else:
                logger.debug('Image selection canceled')
            dialog.destroy()

        dialog.connect('response', on_response)
        dialog.show()
