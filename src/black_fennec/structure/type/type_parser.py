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
    @staticmethod
    def parse(type_map: Map) -> type_base.Type:
        factory_map = {
            "Map": map_type.MapType,
            "List": list_type.ListType,
            "Reference": ReferenceType,
            "Null": NullType,
            "String": StringType,
            "Number": NumberType,
            "Boolean": BooleanType,
        }
        type_name = type_map.value["type"].value
        create_type = factory_map[type_name]
        return create_type(type_map)
