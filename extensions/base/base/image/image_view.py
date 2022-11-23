# -*- coding: utf-8 -*-
import logging
from pathlib import Path

from gi.repository import Gio, Gdk, Gtk, Adw

from base.image.image_view_model import ImageViewModel

from blackfennec.util.change_notification import ChangeNotification

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
        self._view_model.bind(changed=self._update_values)

        self._update_values()

        logger.info('ImageView created')
        self._file_chooser_native = None

    def _set_image_from_path(self, file_path) -> None:
        try:
            paintable = Gdk.Texture.new_from_filename(file_path)
            self._image.set_from_paintable(paintable)
        except Exception as e:
            self._set_image_not_found()
            logger.info(e)

    def _set_image_not_found(self):
        self._image.set_from_icon_name('image-missing-symbolic')

    def _update_values(
            self,
            unused_sender=None,
            unused_notification: ChangeNotification = None):
        self._file_path.set_text(self._view_model.file_path or 'empty path')
        self._set_image_from_path(
            self._view_model.absolute_path)
        self._mime_type.set_text(
            self._view_model.file_type or 'empty mime type')

    @Gtk.Template.Callback()
    def _on_choose_image(self, unused_sender) -> None:
        """Callback for the button click event"""

        dialog = Gtk.FileChooserNative(
            title='Choose file to open',
            transient_for=self.get_root(),
            action=Gtk.FileChooserAction.OPEN,
        )

        document_location = Gio.File.new_for_path(
            self._view_model.location)

        dialog.set_current_folder(document_location)

        filter = Gtk.FileFilter(name='Images')
        filter.add_pixbuf_formats()
        dialog.set_filter(filter)

        def on_response(dialog, response):
            if response == Gtk.ResponseType.ACCEPT:
                liststore = dialog.get_files()
                path = liststore[0].get_path()
                logger.info(f'Chosen file: {path}')
                self._view_model.file_path = path
            else:
                logger.debug('Image selection canceled')
            dialog.destroy()
            self._file_chooser_native = None

        dialog.connect('response', on_response)
        dialog.show()
        self._file_chooser_native = dialog
