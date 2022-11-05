# -*- coding: utf-8 -*-
import json

from blackfennec_doubles.document_system.mime_type.json.double_json_reference_serializer import JsonReferenceSerializerMock
from blackfennec.type_system.type_parser import TypeParser
from blackfennec.structure.map import Map
from blackfennec.structure.string import String
from blackfennec.structure.number import Number
from blackfennec.type_system.type_factory import TypeFactory
from blackfennec.structure.structure_serializer import StructureSerializer


def test_type_from_json():
    json_type = """
{
  "super": null,
  "type": "Map",
  "required": [
    "name"
  ],
  "properties": {
    "name": {
      "super": null,
      "type": "String",
      "pattern": ".{3,}"
    },
    "age": {
      "super": null,
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
    serializer = StructureSerializer(JsonReferenceSerializerMock())
    structure_type = serializer.deserialize(json_type)
    type = TypeParser.parse(structure_type)
    structure = serializer.deserialize(json_object)
    coverage = type.calculate_coverage(structure)
    assert coverage.is_covered()

def test_create_type():
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
