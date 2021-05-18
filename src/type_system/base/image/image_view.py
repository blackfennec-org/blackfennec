# -*- coding: utf-8 -*-
import logging

from gi.repository import Gtk, GdkPixbuf

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
        self._set_file_path(self._view_model.file_path)
        self._set_file_type(self._view_model.file_type)

        logger.info('ImageView created')

    def _set_image_from_path(self, file_path) -> None:
        try:
            pixbuf = self._get_pixbuf(file_path)
            pixbuf = self._rescale_pixbuf(pixbuf, 200)
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
        pixbuf = pixbuf.scale_simple(old_width * scaling, old_height * scaling, 2)
        return pixbuf

    def _calculate_new_image_size_factor(self, width, pixbuf) -> float:
        old_width = pixbuf.get_width()
        factor = width/old_width
        return factor

    def _set_image(self, pixbuf) -> None:
        self._image.set_from_pixbuf(pixbuf)

    def _set_file_path(self, file_path):
        self._view_model.file_path = file_path
        self._file_path_value.set_text(str(file_path))
        self._set_image_from_path(file_path)

    def _set_file_type(self, file_type):
        self._view_model.file_type = file_type
        self._file_type_value.set_text(str(file_type))

    def _set_file_not_found(self):
        self._image.set_from_file('src/type_system/base/image/not-found.png')

    @Gtk.Template.Callback()
    def _on_choose_clicked(self, unused_sender) -> None:
        """Callback for the button click event"""
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
        elif response == Gtk.ResponseType.CANCEL:
            logger.debug('image selection canceled')
        dialog.destroy()

        self._set_file_path(filename)

    @Gtk.Template.Callback()
    def _on_resize(self, unused1, unused2) -> None:
        file_path = self._view_model.file_path
        pixbuf = self._get_pixbuf(file_path)
        width = self.get_allocation().width
        scaled_pixbuf = self._rescale_pixbuf(pixbuf, width - 100)
        self._set_image(scaled_pixbuf)
