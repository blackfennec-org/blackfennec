# -*- coding: utf-8 -*-
from typing import IO

from src.black_fennec.structure.structure import Structure
from src.black_fennec.document_system.mime_type.mime_type import MimeType

import logging
logger = logging.getLogger(__name__)

class InMemoryMimeType(MimeType):

    @property
    def mime_type_id(self) -> str:
        """Returns the mime type id of this mime type e.g. application/json"""
        return 'black_fennec/in_memory'

    def import_structure(self, to_import) -> Structure:
        """Imports a structure from a IO Stream

        Arguments:
            to_import (IO): The IO Stream to import from
        Returns:
            Structure: The imported structure
        """
        return to_import

    def export_structure(self, output: IO, structure: Structure):
        """Exports a structure to a IO Stream

        Arguments:
            output (IO): The IO Stream to export to
            structure (Structure): The structure to export
        """
        logger.warning('Trying to export into an in memory object is a no-op')
