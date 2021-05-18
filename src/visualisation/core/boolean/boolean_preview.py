from gi.repository import Gtk
import logging

logger = logging.getLogger(__name__)


@Gtk.Template(filename='src/visualisation/core/boolean/boolean_preview.glade')
class BooleanPreview(Gtk.Bin):
    """View for the core type Boolean."""

    __gtype_name__ = 'BooleanPreview'
    _value = Gtk.Template.Child()

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (:obj:`BooleanViewModel`): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._value.set_state(self._view_model.value)
        self._value.connect('notify::active', self.on_switch_toggled)

        logger.info(
            'BooleanView with text: "%s" created', self._view_model.value)

    @Gtk.Template.Callback()
    def _on_state_changed(self, unused_sender, state):
        self._view_model.value = state
        if state:
            self.add_style_class('boolean-true')
        else:
            self.add_style_class('boolean-false')

    def on_switch_toggled(self, unused_switch, unused_state):
        if self._value.get_state():
            self.remove_style_class('boolean-false')
            self.add_style_class('boolean-true')
        else:
            self.remove_style_class('boolean-true')
            self.add_style_class('boolean-false')

    def add_style_class(self, class_name):
        my_object = self._value
        object_context = my_object.get_style_context()
        object_context.add_class(class_name)

    def remove_style_class(self, class_name):
        my_object = self._value
        object_context = my_object.get_style_context()
        object_context.remove_class(class_name)

