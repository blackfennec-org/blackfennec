# -*- coding: utf-8 -*-
import logging
import numbers

from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.null import Null
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.string import String
from src.black_fennec.util.document.mime_type.types.json.json_reference_parser import JsonReferenceParser

logger = logging.getLogger(__name__)


class StructureParsingService:
    """Service parses raw json structure into Structure composition"""

    def __init__(self, reference_parser: JsonReferenceParser):
        self._reference_parser = reference_parser

    def _parse(self, raw):
        """Checks if object is an instance of a specific type and
        returns the parsed python object

        Args:
            raw (Any): preparsed JSON

        Returns:
            Structure: Subclass of Structure

        Raises:
            TypeError: If the type contained in the passed json
                could not be recognised.
        """
        if raw is None:
            return self._parse_null()
        if isinstance(raw, dict):
            if self.is_json_reference(raw):
                return self._parse_reference(raw)
            return self._parse_map(raw)
        if isinstance(raw, list):
            return self._parse_list(raw)
        if isinstance(raw, str):
            return StructureParsingService._parse_string(raw)
        if isinstance(raw, bool):
            return StructureParsingService._parse_boolean(raw)
        if isinstance(raw, numbers.Number):
            return StructureParsingService._parse_number(raw)

        message = "Type '{}' not known".format(type(raw))
        logger.error(message)
        raise TypeError(message)

    @staticmethod
    def is_json_reference(dictionary: dict):
        if len(dictionary) == 1 and \
                JsonReferenceParser.JSON_REFERENCE_KEY in dictionary:
            return True
        return False

    def _parse_reference(self, raw):
        """parse json reference_navigation to python reference_navigation"""
        parsed = self._reference_parser.parse(raw)
        return Reference(parsed)

    def _parse_map(self, raw):
        """parse json dict to python map"""
        parsed = {key: self._parse(value) for key, value in raw.items()}
        return Map(parsed)

    def _parse_list(self, raw):
        """parse python list to black fennec list"""
        parsed = [self._parse(value) for value in raw]
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
    def _parse_null():
        return Null()

    def from_json(self, raw):
        return self._parse(raw)
