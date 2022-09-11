# -*- coding: utf-8 -*-
import unittest
from typing import Optional

from doubles.black_fennec.structure.double_structure import StructureInstanceMock
from doubles.black_fennec.structure.double_list import ListInstanceMock
from doubles.black_fennec.structure.double_map import MapInstanceMock
from src.black_fennec.structure.template.template_factory_visitor import TemplateFactoryVisitor
from src.black_fennec.structure.template.list_template import ListTemplate
from src.black_fennec.structure.template.map_template import MapTemplate
from src.black_fennec.structure.template.template_base import TemplateBase
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.black_fennec.structure.number import Number

from src.black_fennec.util.document.mime_type.types.structure_parsing_service import StructureParsingService
import json

class TemplateFactoryVisitorTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor: TemplateFactoryVisitor = TemplateFactoryVisitor()

    def test_can_construct(self):
        pass

    def test_can_visit_structure(self):
        structure = StructureInstanceMock()
        structure_template = self.visitor.visit_structure(structure)
        self.assertIsInstance(structure_template, TemplateBase)

    def test_can_visit_list(self):
        structure_list = ListInstanceMock()
        list_template = self.visitor.visit_list(structure_list)
        self.assertIsInstance(list_template, ListTemplate)

    def test_can_visit_map(self):
        structure_map = MapInstanceMock()
        map_template = self.visitor.visit_map(structure_map)
        self.assertIsInstance(map_template, MapTemplate)

    def test_visit_caches_class(self):
        structure = StructureInstanceMock()
        structure_template_type = type(self.visitor.visit_structure(structure))
        self.assertIsInstance(self.visitor.visit_structure(structure), structure_template_type)

    def test_generic_template_subject(self):
        structure = StructureInstanceMock()
        structure_template = self.visitor.visit_structure(structure).subject
        # checking a property type is not possible thus,
        # only the existence is checked:
        # https://stackoverflow.com/questions/52201094/check-underlying-type-of-a-property-in-python
        self.assertIsNotNone(structure_template)

    def test_template_from_json(self):
        template_factory = self.visitor
        
        json_template = '''
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
        '''
        json_template = json.loads(json_template)
        json_object = '''
{
    "name": "AAA",
    "age": 68
}
        '''
        json_object = json.loads(json_object)

        parser = StructureParsingService()
        structure_template = parser.from_json(json_template)
        template = template_factory.create_template(structure_template)
        structure = parser.from_json(json_object)
        coverage = template.calculate_coverage(structure)
        self.assertTrue(coverage.is_covered())

    def test_create_template(self):
        tf = self.visitor
        
        template = tf.create_map(properties={
          'name': tf.create_string(pattern=".{3,}"),
          'age': tf.create_number(min=0)
        })

        structure = Map({
          'name': String('AAA'),
          'age': Number(68)
        })
        
        coverage = template.calculate_coverage(structure)
        self.assertTrue(coverage.is_covered())
