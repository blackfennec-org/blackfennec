# -*- coding: utf-8 -*-
from typing import IO

from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec.document_system.mime_type.mime_type import MimeType


class MimeTypeMock(MimeType):
    def __init__(
            self,
            mime_type_id="mime_type",
            imported_structure=None,
            exported_structure=None,
    ):
        self._mime_type_id = mime_type_id
        self._imported_structure = imported_structure or StructureMock()
        self._exported_structure = exported_structure
        self.import_structure_parameter_to_import = None
        self.import_structure_count = 0
        self.export_structure_count = 0

    @property
    def mime_type_id(self) -> str:
        return self._mime_type_id

    def import_structure(self, data: IO) -> StructureMock:
        self.import_structure_count += 1
        self.import_structure_parameter_to_import = data.read()
        return self._imported_structure

    def export_structure(self, output: IO, structure):
        self.export_structure_count += 1
        output.write(self._exported_structure)
