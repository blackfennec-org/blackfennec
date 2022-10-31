# -*- coding: utf-8 -*-
import logging
import numbers
from typing import Union

from blackfennec.structure.boolean import Boolean
from blackfennec.structure.list import List
from blackfennec.structure.map import Map
from blackfennec.structure.null import Null
from blackfennec.structure.number import Number
from blackfennec.structure.reference import Reference
from blackfennec.structure.string import String
from blackfennec.structure.structure import Structure
from blackfennec.document_system.mime_type.json.json_reference_serializer import JsonReferenceSerializer

logger = logging.getLogger(__name__)


class StructureSerializer:
    """Serializer allows black-fennec structures to be serialized to native Python datatypes and vice versa"""

    def __init__(self, reference_serializer: JsonReferenceSerializer):
        self._reference_serializer = reference_serializer

    def serialize(self, structure: Structure) -> Union[dict, list, str, bool, numbers.Number, None]:
        """Serializes a black-fennec structure to a native Python datatype

        Arguments:
            structure (Structure): A black-fennec structure
        Returns:
            Union[dict, list, str, bool, numbers.Number, None]: A native Python datatype
        Raises:
            NotImplementedError: If the type contained in the passed Structure is unhandled
        """
        if isinstance(structure, Map):
            return {key: self.serialize(value) for key, value in structure.value.items()}
        if isinstance(structure, List):
            return [self.serialize(item) for item in structure.value]
        if isinstance(structure, Number):
            return structure.value
        if isinstance(structure, String):
            return structure.value
        if isinstance(structure, Boolean):
            return structure.value
        if isinstance(structure, Null):
            return None
        if isinstance(structure, Reference):
            return self._reference_serializer.serialize(structure.value)

        message = "Type '{}' not known".format(type(structure))
        logger.error(message)
        raise NotImplementedError(message)

    def deserialize(self, raw: Union[dict, list, str, bool, numbers.Number, None]) -> Structure:
        """Checks if object is an instance of a specific type and
        returns the parsed black-fennec structure

        Args:
            raw (Union[dict, list, str, bool, numbers.Number, None]): native Python datatype
        Returns:
            Structure: Subclass of Structure
        Raises:
            NotImplementedError: If the type contained in the passed native Python datatype is unhandled.
        """
        if raw is None:
            return Null()
        if isinstance(raw, dict):
            if self._reference_serializer.is_reference(raw):
                return Reference(self._reference_serializer.deserialize(raw))
            else:
                return Map({key: self.deserialize(value) for key, value in raw.items()})
        if isinstance(raw, list):
            return List([self.deserialize(value) for value in raw])
        if isinstance(raw, str):
            return String(raw)
        if isinstance(raw, bool):
            return Boolean(raw)
        if isinstance(raw, numbers.Number):
            return Number(raw)

        message = "Type '{}' not known".format(type(raw))
        logger.error(message)
        raise NotImplementedError(message)
