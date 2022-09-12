# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.black_fennec.structure.double_structure import StructureInstanceMock
from doubles.black_fennec.structure.double_list import ListInstanceMock
from doubles.black_fennec.structure.double_map import MapInstanceMock
from src.black_fennec.structure.template.template_parser import TemplateParser
from src.black_fennec.structure.template.list_template import ListTemplate
from src.black_fennec.structure.template.map_template import MapTemplate
from src.black_fennec.structure.template.template import Template
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.template.template_factory import TemplateFactory

from src.black_fennec.util.document.mime_type.types.structure_parsing_service import (
    StructureParsingService,
)
import json


class TemplateParserTestSuite(unittest.TestCase):
    def setUp(self):
        self.template_parser: TemplateParser = TemplateParser()

    def test_template_from_json(self):
        json_template = """
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
        json_template = json.loads(json_template)
        json_object = """
{
    "name": "AAA",
    "age": 68
}
        """
        json_object = json.loads(json_object)

        parser = StructureParsingService()
        structure_template = parser.from_json(json_template)
        template = self.template_parser.parse(structure_template)
        structure = parser.from_json(json_object)
        coverage = template.calculate_coverage(structure)
        assert coverage.is_covered()

    def test_create_template(self):
        template_factory = TemplateFactory()

        template = template_factory.create_map(
            properties={
                "name": template_factory.create_string(pattern=".{3,}"),
                "age": template_factory.create_number(min=0),
            }
        )

        structure = Map({"name": String("AAA"), "age": Number(68)})

        coverage = template.calculate_coverage(structure)
        assert coverage.is_covered()
