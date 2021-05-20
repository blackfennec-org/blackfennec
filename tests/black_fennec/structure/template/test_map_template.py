import unittest

from doubles.black_fennec.structure.double_info import InfoMock
from doubles.black_fennec.structure.template.double_template_factory_visitor import TemplateFactoryVisitorMock
from doubles.double_dummy import Dummy
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

    def test_calculate_coverage_map_full_coverage(self):
        subject = Map({'info1': InfoMock('Info'), 'info2': InfoMock('Info')})
        template = Map(
            {'info1': InfoMock('Info'), 'info2': InfoMock('Info')}
        )
        map_template = MapTemplate(self.visitor, template)

        coverage = map_template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            (3, 3)
        )

    def test_calculate_coverage_map_half_coverage(self):
        subject = Map({'info1': InfoMock('Info'), 'info2': InfoMock('Info')})
        specificity = 1
        template = Map(
            {'info1': InfoMock('Info')}
        )
        map_template = MapTemplate(self.visitor, template)

        coverage = map_template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            (3, 2)
        )

    def test_calculate_coverage_map_third_coverage(self):
        subject = Map(
            {
                'info1': InfoMock('Info'),
                'info2': InfoMock('Info'),
                'info3': InfoMock('Info')
            }
        )
        template = Map(
            {'info1': InfoMock('Info')}
        )
        map_template = MapTemplate(self.visitor, template)

        coverage = map_template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            (4, 2)
        )

    def test_calculate_coverage_map_unhandleable(self):
        subject = Map(
            {
                'info1': InfoMock('Info')
            }
        )
        template = Map(
            {
                'info1': InfoMock('Info'),
                'info2': InfoMock('Info'),
            }
        )
        map_template = MapTemplate(self.visitor, template)

        coverage = map_template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            (2, 0)
        )

    def test_calculate_coverage_wrong_type(self):
        subject = InfoMock()
        template = Map(
            {'info1': InfoMock('Info'), 'info2': InfoMock('Info')}
        )
        map_template = MapTemplate(self.visitor, template)

        coverage = map_template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            TemplateBase.NOT_COVERED
        )

    def test_can_get_repr(self):
        representation: str = self.map_template.__repr__()
        self.assertTrue(representation.startswith('MapTemplate('))