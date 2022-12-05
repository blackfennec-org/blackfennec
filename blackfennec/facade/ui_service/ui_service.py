from gi.repository import Adw, GLib

from blackfennec.facade.ui_service.message import Message
from blackfennec.util.observable import Observable


class UiService(Observable):
    def __init__(self):
        super().__init__()

    def show_message(self, message: Message):
        adw_toast = Adw.Toast.new(title=message.text)

        if message.action_name and message.action_target:
            adw_toast.set_button_label(message.action_name)
            adw_toast.set_action_name(message.action_target)
        self._notify('message', adw_toast)

    def copy(self):
        return UiService()
