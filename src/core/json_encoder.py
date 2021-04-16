import json

from src.core.types.boolean import Boolean
from src.core.types.list import List
from src.core.types.map import Map
from src.core.types.number import Number
from src.core.types.string import String


class JsonEncoder(json.JSONEncoder):
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
