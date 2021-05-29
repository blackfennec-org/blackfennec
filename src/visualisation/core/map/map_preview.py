from gi.repository import Gtk
import logging

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/visualisation/core/map/map_preview.glade')
class MapPreview(Gtk.Bin):
    """Preview for the core type Map."""

    __gtype_name__ = 'MapPreview'

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (:obj:`MapViewModel`): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        logger.info('MapPreview created')

    @Gtk.Template.Callback()
    def _click_handler(self, unused_sender, unused_argument) -> None:
        """Handles clicks on map items, triggers navigation"""
        self.remove_style_class('is-active')
        self.add_style_class('is-active')
        self._view_model.navigate_to(self._view_model.value)

    def add_style_class(self, class_name):
        my_object = self.get_parent().get_parent().get_parent()
        object_context = my_object.get_style_context()
        object_context.add_class(class_name)

    def remove_style_class(self, class_name):
        my_object = self.get_parent().get_parent()\
            .get_parent().get_parent().get_parent()
        children = my_object.get_children()
        for child in children:
            object_context = child.get_child().get_style_context()
            object_context.remove_class(class_name)
