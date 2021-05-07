# -*- coding: utf-8 -*-
import numbers
import logging

from uri import URI

from src.structure.map import Map
from src.structure.list import List
from src.structure.reference import Reference
from src.structure.string import String
from src.structure.number import Number
from src.structure.boolean import Boolean

logger = logging.getLogger(__name__)


class StructureParsingService:
    """Service parses raw json structure into Info composition"""

    JSON_REFERENCE_KEY = '$ref'

    """StructureParsingService, creates python objects from json"""
    def __init__(self):
        self._reference_resolving_service = None

    def set_reference_resolving_service(self, reference_resolving_service):
        """
        Args:
            reference_resolving_service: The reference resolving service must
                have the `resolve` method
        """
        self._reference_resolving_service = reference_resolving_service

    def _parse(self, raw):
        """Checks if object is an instance of a specific type and
        returns the parsed python object

        Args:
            raw (Any): preparsed JSON

        Returns:
            Info: Subclass of Info

        Raises:
            TypeError: If the type contained in the passed json
                could not be recognised.
        """
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
        if len(dictionary) == 1 and\
                StructureParsingService.JSON_REFERENCE_KEY in dictionary:
            return True
        return False

    def _parse_reference(self, raw):
        """parse json reference to python reference"""
        parsed = URI(raw[StructureParsingService.JSON_REFERENCE_KEY])
        return Reference(self._reference_resolving_service, parsed)

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

    def from_json(self, raw):
        return self._parse(raw)
