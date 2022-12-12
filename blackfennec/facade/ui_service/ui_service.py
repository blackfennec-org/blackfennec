import logging
from io import StringIO

from gi.repository import Gdk, Gtk, Adw, Gio

from blackfennec.actions.context import Context
from blackfennec.document_system.mime_type.mime_type import MimeType
from blackfennec.document_system.mime_type.mime_type_registry import \
    MimeTypeRegistry
from blackfennec.facade.ui_service.message import Message
from blackfennec.facade.ui_service.mime_type_selection.mime_type_selection_view import \
    MimeTypeSelectionDialog

logger = logging.getLogger(__name__)


class UiService:
    def __init__(self, mime_type_registry):
        super().__init__()
        self._mime_type_registry: MimeTypeRegistry = mime_type_registry
        self._message_overlays = {}

    def register_message_overlay(self, message_overlay: Adw.ToastOverlay):
        window = message_overlay.get_root()
        assert window not in self._message_overlays
        self._message_overlays[window] = message_overlay

    def deregister_message_overlay(self, message_overlay: Adw.ToastOverlay):
        window = message_overlay.get_root()
        assert window in self._message_overlays
        del self._message_overlays[window]

    def show_message(self, context: Context, message: Message):
        adw_toast = Adw.Toast.new(title=message.text)

        if message.action_name and message.action_target:
            adw_toast.set_button_label(message.action_name)
            adw_toast.set_action_name(message.action_target)

        self._message_overlays[context.window].add_toast(adw_toast)

    def show_mime_type_selection_dialog(
            self,
            context: Context,
            callback: callable,
            serialized_structure: str,
    ):  # pragma: no cover
        dialog = MimeTypeSelectionDialog(
            self._mime_type_registry,
            serialized_structure,
            transient_for=context.window,
        )

        def on_response(dialog, response):
            if response == Gtk.ResponseType.ACCEPT.value_nick:
                mime_type = dialog.selected_mime_type
                serialized_structure = dialog.serialization_to_determine
                import_input = StringIO(serialized_structure)
                try:
                    structure = mime_type.import_structure(import_input)
                    callback(structure)
                    dialog.destroy()
                except Exception as e:
                    self.show_message(
                        context,
                        Message("Could not import structure")
                    )
            else:
                self.show_message(
                    context,
                    Message("Import cancelled")
                )
                dialog.destroy()

        dialog.connect('response', on_response)
        dialog.present()

    @classmethod
    def set_clipboard(cls, serialized_structure: str):  # pragma: no cover
        clipboard = Gdk.Display.get_default().get_clipboard()
        clipboard.set(serialized_structure)

    @classmethod
    def get_clipboard_async(cls, callback):  # pragma: no cover
        clipboard = Gdk.Display.get_default().get_clipboard()
        clipboard.read_text_async(callback=callback)

    def get_structure_from_clipboard_async(
            self,
            context: Context,
            mime_type: MimeType,
            callback: callable,
    ):  # pragma: no cover
        def deserialize(clipboard: Gdk.Clipboard, res: Gio.Task):
            clipboard_text = clipboard.read_text_finish(res)
            import_input = StringIO(clipboard_text)
            try:
                structure = mime_type.import_structure(import_input)
                callback(structure)
            except Exception as e:
                self.show_mime_type_selection_dialog(
                    context,
                    callback,
                    clipboard_text,
                )

        self.get_clipboard_async(deserialize)

    @classmethod
    def fix_focus(cls, context: Context):  # pragma: no cover
        """By using Gtk.Window.set_focus() without parameters focus is
        reset which can fix the focus in the window. This is a workaround
        for a bug only triggered in Flatpak."""
        context.window.set_focus()
