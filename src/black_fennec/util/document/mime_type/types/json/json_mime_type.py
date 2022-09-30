# -*- coding: utf-8 -*-
import json
from typing import IO

from src.black_fennec.structure.structure import Structure
from src.black_fennec.util.document.mime_type.mime_type import MimeType
from src.black_fennec.util.document.mime_type.types.json.structure_encoding_service import StructureEncodingService
from src.black_fennec.util.document.mime_type.types.json.structure_parsing_service import StructureParsingService


class JsonMimeType(MimeType):
    def __init__(
            self,
            structure_encoding_service: StructureEncodingService,
            structure_parsing_service: StructureParsingService
    ):
        self.structure_encoding_service = structure_encoding_service
        self.structure_parsing_service = structure_parsing_service

    @property
    def mime_type_id(self) -> str:
        return 'application/json'

    def import_structure(self, to_import: IO) -> Structure:
        raw = json.load(to_import)
        return self.structure_parsing_service.from_json(raw)

    def export_structure(self, output: IO, structure: Structure):
        output.write(self.structure_encoding_service.encode(structure))
