# -*- coding: utf-8 -*-

from src.black_fennec.structure.type.type_parser import TypeParser
from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.null import Null
from src.black_fennec.structure.type.type import Type
from .list_type import ListType
from .map_type import MapType
from .null_type import NullType
from .string_type import StringType
from .number_type import NumberType
from .boolean_type import BooleanType


class TypeFactory:
    @classmethod
    def create_map(cls, properties=None, type="Map", super: Type = None):
        if super:
            super_struct = super.subject
        else:
            super_struct = Null()
        type = MapType(
            Map(
                {
                    "super": super_struct,
                    "type": String(type),
                    "required": List(),
                    "properties": Map(),
                }
            ),
        )

        if properties:
            for name, value in properties.items():
                type.add_property(name, value)

        return type

    @classmethod
    def create_list(cls):
        type = ListType(
            Map(
                {
                    "super": Null(),
                    "type": String("List"),
                    "required": List(),
                    "elements": List(),
                }
            ),
        )
        return type

    @classmethod
    def create_string(cls, pattern=".*", default=""):
        return StringType(
            Map(
                {
                    "super": Null(),
                    "type": String("String"),
                    "pattern": String(pattern),
                    "default": String(default),
                }
            ),
        )

    @classmethod
    def create_number(cls, min=None, max=None, default=0):
        return NumberType(
            Map(
                {
                    "super": Null(),
                    "type": String("Number"),
                    "default": Number(default),
                    "minimum": Null(),
                    "maximum": Null(),
                }
            ),
        )

    @classmethod
    def create_boolean(cls, expected=None, default=False):
        if expected:
            expected = Boolean(expected)
        else:
            expected = Null()

        return BooleanType(
            Map(
                {
                    "super": Null(),
                    "type": String("Boolean"),
                    "default": Boolean(default),
                    "expected": expected,
                }
            ),
        )

    @classmethod
    def create_null(cls):
        return NullType(
            Map(
                {
                    "super": Null(),
                    "type": String("Null"),
                }
            ),
        )
