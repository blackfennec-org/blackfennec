import logging
from io import StringIO

from gi.repository import Gdk, Gio

from blackfennec.actions.action import Action
from blackfennec.actions.context import Context
from blackfennec.document_system.document import Document
from blackfennec.document_system.document_registry import DocumentRegistry
from blackfennec.document_system.mime_type.mime_type import MimeType
from blackfennec.structure.list import List
from blackfennec.structure.map import Map
from blackfennec.structure.structure import Structure
from blackfennec.type_system.type import Type

logger = logging.getLogger(__name__)


class PasteAction(Action):
    def __init__(self, type: Type, document_registry: DocumentRegistry):
        super().__init__(type)
        self._document_registry = document_registry

    @classmethod
    def _get_structure_from_clipboard_async(
            cls,
            mime_type: MimeType,
            callback: callable,
    ):  # pragma: no cover
        def deserialize(clipboard: Gdk.Clipboard, res: Gio.Task):
            clipboard_text = clipboard.read_text_finish(res)
            import_input = StringIO(clipboard_text)
            structure = mime_type.import_structure(import_input)
            callback(structure)

        clipboard = Gdk.Display.get_default().get_clipboard()
        clipboard.read_text_async(callback=deserialize)

    @staticmethod
    def get_item_key(map: Map, item: Structure):
        context_key = None
        for key, value in map.structure.value.items():
            if value == item.structure:
                context_key = key
                break
        assert context_key is not None
        return context_key

    def execute(self, context: Context):
        to_replace = context.structure
        document: Document = self._document_registry.get_document(
            context.structure.structure
        )

        def replace_with_clipboard(replacement: Structure):
            if to_replace.parent:
                if isinstance(to_replace.parent.structure, Map):
                    parent_map: Map = to_replace.parent
                    context_key = self.get_item_key(parent_map, to_replace)
                    parent_map.remove_item(context_key)
                    parent_map.add_item(context_key, replacement)
                elif isinstance(to_replace.parent.structure, List):
                    parent_list: List = to_replace.parent
                    parent_list.remove_item(to_replace)
                    parent_list.add_item(replacement)
                else:
                    raise NotImplementedError(
                        "Pasting into a non-map or non-list is not implemented"
                    )
            else:
                if isinstance(context.structure, type(replacement.structure)):
                    context.structure.value = replacement.structure.value
                else:
                    message = "Cannot paste structure if not same type."
                    logger.warning(message)
                    raise TypeError(message)

        self._get_structure_from_clipboard_async(
            document.mime_type,
            callback=replace_with_clipboard,
        )

    @property
    def name(self):
        return "replace with clipboard"

    @property
    def description(self):
        return """Pastes the structure from the Clipboard which is expected
            to be serialized in the same mime_type as the opened Document."""
