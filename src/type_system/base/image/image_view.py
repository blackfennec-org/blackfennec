# -*- coding: utf-8 -*-
import logging

from gi.repository import Gtk

from src.type_system.base.image.image_view_model import ImageViewModel

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/type_system/base/image/image_view.glade')
class ImageView(Gtk.Bin):
    """View for the core type Image."""

    __gtype_name__ = 'ImageView'
    _file_path_value: Gtk.Label = Gtk.Template.Child()
    _file_type_value: Gtk.Label = Gtk.Template.Child()
    _image: Gtk.Image = Gtk.Template.Child()

    def __init__(self, view_model: ImageViewModel):
        """Construct with view_model.

        Args:
            view_model (ImageViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._set_file_path()
        self._set_file_type()
        logger.info(
            'ImageView created'
        )

    def _set_file_path(self):
        file_path = self._view_model.file_path
        self._file_path_value.set_text(str(file_path))
        self._image.set_from_file(file_path)

    def _set_file_type(self):
        file_type = self._view_model.file_type
        self._file_type_value.set_text(str(file_type))

    @Gtk.Template.Callback()
    def on_choose_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
        logger.debug('choose clicked')
        dialog = Gtk.FileChooserDialog(
            title='Please choose a image',
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
            logger.debug('image selection canceled')

        dialog.destroy()
