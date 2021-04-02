import json
import numbers
from src.core.map import Map
from src.core.list import List
from src.core.string import String
from src.core.number import Number
from src.core.boolean import Boolean


class JsonEncoder(json.JSONEncoder):
    """Json Encoder"""

    def default(self, obj):
        return obj.value


class JsonParser:
    """JsonParser, creates python objects from json"""

    @staticmethod
    def _parse(raw):
        """Checks if object is an instance of a specific type and
        returns the parsed python object

        Args:
            raw: preparsed JSON
        """
        if isinstance(raw, dict):
            return JsonParser._parse_map(raw)
        if isinstance(raw, list):
            return JsonParser._parse_list(raw)
        if isinstance(raw, str):
            return JsonParser._parse_string(raw)
        if isinstance(raw, bool):
            return JsonParser._parse_boolean(raw)
        if isinstance(raw, numbers.Number):
            return JsonParser._parse_number(raw)

        raise Exception("Type '{}' not known".format(type(raw)))

    @staticmethod
    def _parse_map(raw):
        """parse json dict to python map"""
        parsed = {key: JsonParser._parse(value) for key, value in raw.items()}
        return Map(parsed)

    @staticmethod
    def _parse_list(raw):
        """parse python list to black fennec list"""
        parsed = [JsonParser._parse(value) for value in raw]
        return List(parsed)

    @staticmethod
    def _parse_string(raw):
        """parse python string to black fennec string"""
        return String(raw)

    @staticmethod
    def _parse_number(raw):
        """parse python number to black fennec number"""
        return Number(raw)

    @staticmethod
    def _parse_boolean(raw):
        """parse python boolean to black fennec boolean"""
        return Boolean(raw)

    @staticmethod
    def from_json(raw):
        return JsonParser._parse(raw)
