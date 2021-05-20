# -*- coding: utf-8 -*-
import json

from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.string import String


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
