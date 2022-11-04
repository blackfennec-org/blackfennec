from pathlib import Path

from gi.repository import Gtk, Adw
import logging

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('boolean_view.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class BooleanView(Adw.Bin):
    """View for the core type Boolean."""

    __gtype_name__ = 'BooleanView'
    _value = Gtk.Template.Child()

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (BooleanViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._value.set_state(self._view_model.value)
        self._initiate_state_style()
        self._value.connect('notify::active', self._on_switch_toggled)

        logger.info(
            'BooleanView with text: "%s" created', self._view_model.value)

    @Gtk.Template.Callback()
    def _on_state_changed(self, unused_sender, state):
        self._view_model.value = state
        if state:
            self.add_style_class('boolean-true')
        else:
            self.add_style_class('boolean-false')

    def _on_switch_toggled(self, unused_switch, unused_state):
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

    def _initiate_state_style(self):
        state = self._value.get_active()
        if state:
            self.add_style_class('boolean-true')
        else:
            self.add_style_class('boolean-false')