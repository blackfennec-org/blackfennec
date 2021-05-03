import unittest
from typing import Optional

from doubles.double_dummy import Dummy
from doubles.structure.double_info import InfoMock
from doubles.structure.double_map import MapMock
from doubles.structure.template.double_template_factory import TemplateFactoryMock
from src.structure.info import Info
from src.structure.map import Map
from src.structure.root import Root
from src.structure.template.map_template import MapTemplate
from src.structure.template.template_factory import _get_template_class


class MapTemplateTestSuite(unittest.TestCase):
    def setUp(self):
        self.property_storage = dict()
        self.factory = TemplateFactoryMock()
        self.subject = Map()
        self.subject.parent = Root(self.subject)
        self.map_template: Optional[MapTemplate] = MapTemplate(self.subject, self.factory, self.property_storage)

    def tearDown(self) -> None:
        self.property_storage = None
        self.factory = None
        self.subject = None
        self.map_template: Optional[MapTemplate] = None

    def test_can_create(self):
        pass

    def test_subject_getter(self):
        self.assertEqual(self.map_template.subject, self.subject)

    def test_get_item(self):
        key = 'test'
        value = InfoMock('test_value')
        self.subject[key] = value
        self.factory._create_return = value
        map_template: Optional[MapTemplate] = MapTemplate(self.subject, self.factory, self.property_storage)
        get = map_template[key]
        self.assertEqual(get, value)
        self.assertEqual(self.factory._subject, value)
        self.assertEqual(self.factory._create_calls, 1)

    def test_set_item(self):
        key = 'test'
        value = InfoMock('test_value')
        self.factory._create_return = value
        self.map_template[key] = value
        self.assertEqual(value, self.map_template[key])

    def test_set_item_already_encapsulated(self):
        key = 'test'
        value = InfoMock('test_value')
        template_class = _get_template_class(Info)
        encapsulated = template_class(value, self.factory, None)
        self.factory._create_return = encapsulated
        self.factory._create_return = value
        self.map_template[key] = encapsulated
        self.assertEqual(value, self.map_template[key])

    def test_get_children(self):
        key = 'test'
        value = InfoMock('test_value')
        self.subject[key] = value
        self.factory._create_return = value
        map_template: Optional[MapTemplate] = MapTemplate(self.subject, self.factory, self.property_storage)
        children = map_template.children
        self.assertEqual(len(children), 1)
        self.assertEqual(self.factory._subject, value)
        self.assertEqual(self.factory._create_calls, 1)

    def test_get_empty_children(self):
        children = self.map_template.children
        self.assertEqual(len(children), 0)
        self.assertEqual(self.factory._create_calls, 0)

    def test_can_get_repr(self):
        representation: str = self.map_template.__repr__()
        self.assertTrue(representation.startswith('MapTemplate('))
