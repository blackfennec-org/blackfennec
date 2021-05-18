import unittest

from doubles.black_fennec.structure.double_info import InfoMock
from doubles.black_fennec.structure.template.double_template_factory_visitor import TemplateFactoryVisitorMock
from src.black_fennec.structure.encapsulation_base.base_factory_visitor import _create_generic_class
from src.black_fennec.structure.info import Info
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.root import Root
from src.black_fennec.structure.template.map_template import MapTemplate
from src.black_fennec.structure.template.template_base import TemplateBase
from src.visualisation.base.date_time_range.date_time_range import DateTimeRange


class MapTemplateTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = TemplateFactoryVisitorMock()
        self.subject = Map()
        self.subject.parent = Root(self.subject)
        self.map_template = MapTemplate(self.visitor, self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.map_template = None

    def test_can_construct(self):
        pass

    def test_set_item_already_encapsulated(self):
        key = 'test'
        value = InfoMock('test_value')
        template_class = _create_generic_class(TemplateBase, Info)
        encapsulated = template_class(self.visitor, value)
        self.map_template[key] = encapsulated
        self.assertEqual(value, self.map_template[key].subject)

    def test_set_item_map_already_encapsulated(self):
        key = 'test'
        value = Map()
        encapsulated = MapTemplate(self.visitor, value)
        self.map_template[key] = encapsulated
        self.assertEqual(value, self.map_template[key].subject)

    def test_set_item_other_template(self):
        key = 'test'
        encapsulated = DateTimeRange.TEMPLATE
        value = encapsulated.subject
        self.map_template[key] = encapsulated
        self.assertEqual(value, self.map_template[key].subject)
        self.assertEqual(self.map_template[key].subject.__class__, Map)

    def test_can_get_repr(self):
        representation: str = self.map_template.__repr__()
        self.assertTrue(representation.startswith('MapTemplate('))