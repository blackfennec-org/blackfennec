# -*- coding: utf-8 -*-
import json
from typing import IO

from src.black_fennec.structure.structure import Structure
from src.black_fennec.util.document.mime_type.mime_type import MimeType
from src.black_fennec.util.document.mime_type.types.structure_encoding_service import StructureEncodingService
from src.black_fennec.util.document.mime_type.types.structure_parsing_service import StructureParsingService


class JsonMimeType(MimeType):
    def __init__(
            self,
            structure_encoding_service: StructureEncodingService = None,
            structure_parsing_service: StructureParsingService = None):
        self._structure_encoding_service = structure_encoding_service or StructureEncodingService(indent=2)
        self._structure_parsing_service = structure_parsing_service or StructureParsingService()

    @property
    def mime_type_id(self) -> str:
        return 'application/json'

    def import_structure(self, to_import: IO) -> Structure:
        raw = json.load(to_import)
        return self._structure_parsing_service.from_json(raw)

    def export_structure(self, structure) -> str:
        return self._structure_encoding_service.encode(structure)
