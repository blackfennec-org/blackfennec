from gi.repository import Gtk
import logging

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/type_system/core/list/list_preview.glade')
class ListPreview(Gtk.Bin):
    """Preview for the core type List"""

    __gtype_name__ = 'ListPreview'

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (:obj:`ListViewModel`): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        logger.info('ListPreview created')

    @Gtk.Template.Callback()
    def _click_handler(self, unused_sender, unused_argument) -> None:
        """Handles clicks on list items, triggers navigation"""
        self._view_model.navigate_to(self._view_model.value)
        self.remove_style_class('is-active')
        self.add_style_class('is-active')

    def add_style_class(self, class_name):
        my_object = self.get_parent().get_parent()
        object_context = my_object.get_style_context()
        object_context.add_class(class_name)

    def remove_style_class(self, class_name):
        my_object = self.get_parent().get_parent().get_parent().get_parent()
        children = my_object.get_children()
        for child in children:
            object_context = child.get_child().get_style_context()
            object_context.remove_class(class_name)
