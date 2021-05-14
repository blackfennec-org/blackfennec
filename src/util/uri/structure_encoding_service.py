# -*- coding: utf-8 -*-
import json

from src.structure.boolean import Boolean
from src.structure.list import List
from src.structure.map import Map
from src.structure.number import Number
from src.structure.string import String


class StructureEncodingService(json.JSONEncoder):
    """Json Encoder"""

    def default(self, obj):
        """Checks if obj is instance of specific type and returns obj"""
        if isinstance(obj, Map):
            return obj.data
        if isinstance(obj, List):
            return obj.data
        if isinstance(obj, Number):
            return obj.value
        if isinstance(obj, String):
            return obj.data
        if isinstance(obj, Boolean):
            return obj.value
