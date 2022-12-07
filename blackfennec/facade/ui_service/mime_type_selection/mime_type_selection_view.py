import logging
from pathlib import Path

from gi.repository import Gtk, Adw, GObject

from blackfennec.document_system.mime_type.in_memory.in_memory_mime_type import \
    InMemoryMimeType
from blackfennec.document_system.mime_type.mime_type import MimeType
from blackfennec.document_system.mime_type.mime_type_registry import \
    MimeTypeRegistry

logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
UI_TEMPLATE = str(BASE_DIR.joinpath("mime_type_selection.ui"))


@Gtk.Template(filename=UI_TEMPLATE)
class MimeTypeSelectionDialog(Adw.MessageDialog):
    """Mime type selection dialog."""
    __gtype_name__ = "MimeTypeSelectionView"
    _mime_type_selection: Gtk.ComboBoxText = Gtk.Template.Child()
    _serialization_to_determine: Gtk.TextView = Gtk.Template.Child()

    def __init__(
            self,
            mime_type_registry: MimeTypeRegistry,
            serialization: str = None,
    ):
        super().__init__()

        self._mime_type_registry = mime_type_registry
        self.add_response(Gtk.ResponseType.CANCEL.value_nick, 'Cancel')
        self.add_response(Gtk.ResponseType.ACCEPT.value_nick,
                          'Select')

        self.set_response_appearance(Gtk.ResponseType.ACCEPT.value_nick,
                                     Adw.ResponseAppearance.SUGGESTED)
        self.set_response_appearance(Gtk.ResponseType.CANCEL.value_nick,
                                     Adw.ResponseAppearance.DESTRUCTIVE)

        self.init_mime_type_list_box()

        if serialization:
            self._serialization_to_determine.get_buffer().set_text(
                serialization)
            self._serialization_to_determine.set_visible(True)

    def init_mime_type_list_box(self):
        mime_type_list_store = Gtk.ListStore(GObject.TYPE_STRING)
        mime_types = self._mime_type_registry.mime_types
        for mime_type_id in mime_types.keys():
            if mime_type_id == InMemoryMimeType().mime_type_id:
                continue
            mime_type_list_store.append((mime_type_id,))
        self._mime_type_selection.set_model(mime_type_list_store)

    @property
    def selected_mime_type(self) -> MimeType:
        selected = self._mime_type_selection.get_active_text()
        return self._mime_type_registry.mime_types[selected]

    @property
    def serialization_to_determine(self) -> str:
        buffer = self._serialization_to_determine.get_buffer()
        start = buffer.get_start_iter()
        end = buffer.get_end_iter()
        return buffer.get_text(
            start,
            end,
            True
        )
