# -*- coding: utf-8 -*-
import json

from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.string import String
from src.black_fennec.util.document.mime_type.types.json.json_reference_parser import JsonReferenceParser
from src.black_fennec.util.document.mime_type.types.json.json_reference_serializer import JsonReferenceSerializer
from src.black_fennec.util.document.mime_type.types.json.structure_parsing_service import StructureParsingService


class StructureEncodingService(json.JSONEncoder):
    """Json Encoder"""

    def default(self, obj):
        """Checks if obj is instance of specific type and returns obj"""
        if isinstance(obj, Map):
            return obj.value
        if isinstance(obj, List):
            return obj.value
        if isinstance(obj, Number):
            return obj.value
        if isinstance(obj, String):
            return obj.value
        if isinstance(obj, Boolean):
            return obj.value
        if isinstance(obj, Reference):
            return {
                JsonReferenceParser.JSON_REFERENCE_KEY: JsonReferenceSerializer.serialize(obj.value)
            }
