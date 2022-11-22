from pathlib import Path

from gi.repository import Gtk, Adw

from blackfennec.util.change_notification import ChangeNotification


BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath('number_preview.ui'))


@Gtk.Template(filename=UI_TEMPLATE)
class NumberPreview(Adw.Bin):
    """View for the core type Number"""

    __gtype_name__ = 'NumberPreview'
    _value = Gtk.Template.Child()

    def __init__(self, view_model):
        """Construct with view_model.

        Args:
            view_model (NumberViewModel): The view_model.
        """
        super().__init__()
        self._view_model = view_model
        self._view_model.bind(changed=self._update_value)

        self._value.set_text(str(self._view_model.number.value))

    @Gtk.Template.Callback()
    def _on_text_changed(self, unused_sender):
        text = self._value.get_text()
        digits_string = ''.join([i for i in text if i in '0123456789.,eE-+'])
        if str(self._view_model.number.value) == digits_string:
            return
        try:
            if not float(digits_string).is_integer():
                self._view_model.number.value = float(digits_string)
            else:
                self._view_model.number.value = int(digits_string)

            self._set_icon_valid()
        except Exception:
            self._set_icon_invalid()

    def _update_value(self, unused_sender, notification: ChangeNotification):
        text = self._value.get_text()
        if text == str(notification.new_value):
            return

        self._set_icon_valid()
        self._value.set_text(str(notification.new_value))

    def _set_icon_valid(self):
        self._value.set_icon_from_icon_name(
            Gtk.EntryIconPosition.SECONDARY,
            None
        )
        self._value.set_icon_tooltip_text(
            Gtk.EntryIconPosition.SECONDARY,
            None
        )

    def _set_icon_invalid(self):
        self._value.set_icon_from_icon_name(
            Gtk.EntryIconPosition.SECONDARY,
            'dialog-warning-symbolic'
        )
        self._value.set_icon_tooltip_text(
            Gtk.EntryIconPosition.SECONDARY,
            'Invalid number'
        )
