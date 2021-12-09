import unittest

from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.template.double_template_factory_visitor import TemplateFactoryVisitorMock
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.encapsulation_base.base_factory_visitor import _create_generic_class
from src.black_fennec.structure.structure import Structure
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
        value = StructureMock('test_value')
        template_class = _create_generic_class(TemplateBase)
        encapsulated = template_class(self.visitor, value)
        self.map_template.add_item(key, encapsulated)
        self.assertEqual(value, self.map_template.value[key].subject)

    def test_set_item_map_already_encapsulated(self):
        key = 'test'
        value = Map()
        encapsulated = MapTemplate(self.visitor, value)
        self.map_template.add_item(key, encapsulated)
        self.assertEqual(value, self.map_template.value[key].subject)

    def test_set_item_other_template(self):
        key = 'test'
        encapsulated = DateTimeRange.TEMPLATE
        value = encapsulated.subject
        self.map_template.add_item(key, encapsulated)
        self.assertEqual(value, self.map_template.value[key].subject)
        self.assertEqual(self.map_template.value[key].subject.__class__, Map)

    def test_calculate_coverage_map_full_coverage(self):
        subject = Map({'structure1': StructureMock('Structure'), 'structure2': StructureMock('Structure')})
        template = Map(
            {'structure1': StructureMock('Structure'), 'structure2': StructureMock('Structure')}
        )
        map_template = MapTemplate(self.visitor, template)

        coverage = map_template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            Coverage(3, 3)
        )

    def test_calculate_coverage_map_half_coverage(self):
        subject = Map({'structure1': StructureMock('Structure'), 'structure2': StructureMock('Structure')})
        template = Map(
            {'structure1': StructureMock('Structure')}
        )
        map_template = MapTemplate(self.visitor, template)

        coverage = map_template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            Coverage(3, 2)
        )

    def test_calculate_coverage_map_third_coverage(self):
        subject = Map(
            {
                'structure1': StructureMock('Structure'),
                'structure2': StructureMock('Structure'),
                'structure3': StructureMock('Structure')
            }
        )
        template = Map(
            {'structure1': StructureMock('Structure')}
        )
        map_template = MapTemplate(self.visitor, template)

        coverage = map_template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            Coverage(4, 2)
        )

    def test_calculate_coverage_map_unhandleable(self):
        subject = Map(
            {
                'structure1': StructureMock('Structure')
            }
        )
        template = Map(
            {
                'structure1': StructureMock('Structure'),
                'structure2': StructureMock('Structure'),
            }
        )
        map_template = MapTemplate(self.visitor, template)

        coverage = map_template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            Coverage(2, 0)
        )

    def test_calculate_coverage_wrong_type(self):
        subject = StructureMock()
        template = Map(
            {'structure1': StructureMock('Structure'), 'structure2': StructureMock('Structure')}
        )
        map_template = MapTemplate(self.visitor, template)

        coverage = map_template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            Coverage.NOT_COVERED
        )

    def test_can_create_structure(self):
        map_structure = self.map_template.create_structure()
        self.assertIsInstance(map_structure, Map)

    def test_can_get_repr(self):
        representation: str = self.map_template.__repr__()
        self.assertTrue(representation.startswith('MapTemplate('))
