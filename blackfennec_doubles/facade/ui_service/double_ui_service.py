from blackfennec.util.observable import Observable
from blackfennec_doubles.structure.double_string import StringMock


class UiServiceMock:
    def __init__(self, context=None):
        super().__init__()
        self.copy_count = 0
        self.show_message_count = 0
        self.show_message_parameter_context = None
        self.show_message_parameter_message = None
        self.set_clipboard_count = 0
        self.set_clipboard_parameter = None
        self.get_structure_from_clipboard_async_count = 0
        self.get_structure_from_clipboard_async_parameter_context = None
        self.get_structure_from_clipboard_async_parameter_mime_type = None
        self.get_structure_from_clipboard_async_parameter_callback = None

    def copy(self):
        self.copy_count += 1
        return self

    def show_message(self, context, message):
        self.show_message_count += 1
        self.show_message_parameter_context = context
        self.show_message_parameter_message = message

    def set_clipboard(self, text):
        self.set_clipboard_parameter = text
        self.set_clipboard_count += 1

    def get_structure_from_clipboard_async(self, context, mime_type, callback):
        self.get_structure_from_clipboard_async_parameter_context = context
        self.get_structure_from_clipboard_async_parameter_mime_type = mime_type
        self.get_structure_from_clipboard_async_parameter_callback = callback
        self.get_structure_from_clipboard_async_count += 1
