# -*- coding: utf-8 -*-
from src.black_fennec.util.parameterized_visitor import ParameterizedVisitor
from src.black_fennec.structure.map import Map

import src.black_fennec.structure.type.list_type as list_type
import src.black_fennec.structure.type.map_type as map_type
import src.black_fennec.structure.type.type as type_base
from .reference_type import ReferenceType
from .null_type import NullType
from .string_type import StringType
from .number_type import NumberType
from .boolean_type import BooleanType


class TypeParser(ParameterizedVisitor):
    @classmethod
    def _get_core_type(cls, structure: Map):
        if structure.value["super"].value is not None:
            return cls._get_core_type(structure.value["super"])
        return structure.value["type"].value
        

    @classmethod
    def parse(cls, structure: Map) -> type_base.Type:
        factory_map = {
            "Map": map_type.MapType,
            "List": list_type.ListType,
            "Reference": ReferenceType,
            "Null": NullType,
            "String": StringType,
            "Number": NumberType,
            "Boolean": BooleanType,
        }
        type_name = cls._get_core_type(structure)
        create_type = factory_map[type_name]
        return create_type(structure)
