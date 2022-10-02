# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.black_fennec.structure.double_structure import StructureInstanceMock
from doubles.black_fennec.structure.double_list import ListInstanceMock
from doubles.black_fennec.structure.double_map import MapInstanceMock
from src.black_fennec.structure.type.type_parser import TypeParser
from src.black_fennec.structure.type.list_type import ListType
from src.black_fennec.structure.type.map_type import MapType
from src.black_fennec.structure.type.type import Type
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.type.type_factory import TypeFactory

from src.black_fennec.util.document.mime_type.types.structure_parsing_service import (
    StructureParsingService,
)
import json


class TypeParserTestSuite(unittest.TestCase):
    def setUp(self):
        self.type_parser: TypeParser = TypeParser()

    def test_type_from_json(self):
        json_type = """
{
  "type": "Map",
  "required": [
    "name"
  ],
  "properties": {
    "name": {
      "type": "String",
      "pattern": ".{3,}"
    },
    "age": {
      "type": "Number",
      "minimum": 0
    }
  }
}
        """
        json_type = json.loads(json_type)
        json_object = """
{
    "name": "AAA",
    "age": 68
}
        """
        json_object = json.loads(json_object)

        parser = StructureParsingService()
        structure_type = parser.from_json(json_type)
        type = self.type_parser.parse(structure_type)
        structure = parser.from_json(json_object)
        coverage = type.calculate_coverage(structure)
        assert coverage.is_covered()

    def test_create_type(self):
        type_factory = TypeFactory()

        type = type_factory.create_map(
            properties={
                "name": type_factory.create_string(pattern=".{3,}"),
                "age": type_factory.create_number(min=0),
            }
        )

        structure = Map({"name": String("AAA"), "age": Number(68)})

        coverage = type.calculate_coverage(structure)
        assert coverage.is_covered()
