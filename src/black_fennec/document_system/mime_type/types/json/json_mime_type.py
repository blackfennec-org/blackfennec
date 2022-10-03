# -*- coding: utf-8 -*-
import json
from typing import IO

from src.black_fennec.structure.structure import Structure
from src.black_fennec.document_system.mime_type.mime_type import MimeType
from src.black_fennec.document_system.mime_type.types.json.structure_serializer import StructureSerializer


class JsonMimeType(MimeType):
    def __init__(
            self,
            structure_serializer: StructureSerializer,
    ):
        self._structure_serializer = structure_serializer

    @property
    def mime_type_id(self) -> str:
        """Returns the mime type id of this mime type e.g. application/json"""
        return 'application/json'

    def import_structure(self, to_import: IO) -> Structure:
        """Imports a structure from a IO Stream

        Arguments:
            to_import (IO): The IO Stream to import from
        Returns:
            Structure: The imported structure
        """
        raw = json.load(to_import)
        return self._structure_serializer.deserialize(raw)

    def export_structure(self, output: IO, structure: Structure):
        """Exports a structure to a IO Stream

        Arguments:
            output (IO): The IO Stream to export to
            structure (Structure): The structure to export
        """
        raw = self._structure_serializer.serialize(structure)
        json.dump(raw, output)
