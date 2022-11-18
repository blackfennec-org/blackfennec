import logging
from io import StringIO

from blackfennec.actions.action import Action
from blackfennec.actions.context import Context
from blackfennec.document_system.document import Document
from blackfennec.document_system.document_registry import DocumentRegistry
from blackfennec.type_system.type import Type

from gi.repository import Gdk

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class CopyAction(Action):
    def __init__(self, type: Type, document_registry: DocumentRegistry):
        super().__init__(type)
        self._document_registry = document_registry

    def execute(self, context: Context):
        document: Document = self._document_registry.get_document(
            context.structure.structure
        )
        export_output = StringIO()
        document.mime_type.export_structure(
            export_output,
            context.structure.structure,
        )
        export_output.seek(0)
        serialized_structure = export_output.read()

        clipboard = Gdk.Display.get_default().get_clipboard()
        clipboard.set(serialized_structure)

    @property
    def name(self):
        return "copy"

    @property
    def description(self):
        return """Copies the structure to the clipboard."""
