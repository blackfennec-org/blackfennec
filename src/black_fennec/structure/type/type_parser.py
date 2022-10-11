# -*- coding: utf-8 -*-
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.merge.deep_merge import DeepMerge

import src.black_fennec.structure.type.list_type as list_type
import src.black_fennec.structure.type.map_type as map_type
from .reference_type import ReferenceType
from .null_type import NullType
from .string_type import StringType
from .number_type import NumberType
from .boolean_type import BooleanType

import logging
logger = logging.getLogger(__name__)

class TypeParser:
    FACTORIES = {
        "Map": map_type.MapType,
        "List": list_type.ListType,
        "Reference": ReferenceType,
        "Null": NullType,
        "String": StringType,
        "Number": NumberType,
        "Boolean": BooleanType,
    }

    @classmethod
    def _merge_super(cls, structure):
        logger.debug(f"Merge super for {structure}")
        super = structure.value["super"]
        if super.value is None:
            return structure
        merged_super = cls._merge_super(super)
        return DeepMerge.merge(underlay=merged_super, overlay=structure)

    @classmethod
    def _get_core_type(cls, structure: Map):
        if structure.value["super"].value is not None:
            return cls._get_core_type(structure.value["super"])
        return structure.value["type"].value

    @classmethod
    def parse(cls, structure: Map):
        structure = cls._merge_super(structure)
        type_name = cls._get_core_type(structure)
        create_type = cls.FACTORIES[type_name]
        return create_type(structure)
