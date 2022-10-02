# -*- coding: utf-8 -*-

from src.black_fennec.structure.list import List
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.null import Null
from .list_type import ListType
from .map_type import MapType
from .null_type import NullType
from .string_type import StringType
from .number_type import NumberType
from .boolean_type import BooleanType


class TypeFactory:
    @staticmethod
    def create_map(properties=None):
        type = MapType(
            Map({
                "type": String("Map"), 
                "required": List(), 
                "properties": Map()}),
        )

        if properties:
            for name, value in properties.items():
                type.add_property(name, value)

        return type


    @staticmethod
    def create_list():
        type = ListType(
            Map({
                "type": String("List"),
                "required": List(),
                "elements": List()
            })
        )
        return type


    @staticmethod
    def create_string(pattern=".*", default=""):
        return StringType(
            Map(
                {
                    "type": String("String"),
                    "pattern": String(pattern),
                    "default": String(default),
                }
            ),
        )


    @staticmethod
    def create_number(min=None, max=None, default=0):
        return NumberType(
            Map({
                "type": String("Number"), 
                "default": Number(default),
                "minimum": Null(),
                "maximum": Null()
            }),
        )


    @staticmethod
    def create_boolean(expected=None, default=False):
        if expected:
            expected = Boolean(expected)
        else:
            expected = Null()
        
        return BooleanType(
            Map({
                "type": String("Boolean"), 
                "default": Boolean(default),
                "expected": expected
            })
        )


    @staticmethod
    def create_null():
        return NullType(
            Map({
                "type": String("Null"), 
            })
        )

