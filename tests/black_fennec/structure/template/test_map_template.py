import unittest

from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.double_string import StringMock
from doubles.black_fennec.structure.template.double_template_factory_visitor import TemplateFactoryVisitorMock
from doubles.black_fennec.structure.template.double_template import TemplateMock
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.encapsulation_base.base_factory_visitor import _create_generic_class
from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.list import List
from src.black_fennec.structure.string import String
from src.black_fennec.structure.template.template_factory_visitor import TemplateFactoryVisitor
from src.black_fennec.structure.template.map_template import MapTemplate
from src.black_fennec.structure.template.template_base import TemplateBase
from src.visualisation.base.date_time_range.date_time_range import DateTimeRange


class MapTemplateTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = TemplateFactoryVisitorMock()
        self.subject = Map({'type': String('Map'), 'required': List(), 'properties': Map()})
        self.map_template = MapTemplate(self.visitor, self.subject)


    def test_can_construct(self):
        pass

    def test_set_item_already_encapsulated(self):
        key = 'test'
        value = StringMock('test_value')
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
        subject = Map({'structure1': StringMock('Structure'), 'structure2': StringMock('Structure')})
        '''
        # we are not testing the factory, but this is how we would.
        template_structure = Map(
            {
                'type': String('Map'),
                'requires': List(),
                'properties': Map({
                    'structure1': TemplateMock('Structure'), 
                    'structure2': TemplateMock('Structure')
                })
            }
        )
        template = MapTemplate(self.visitor, template_structure)
        '''
        template = TemplateFactoryVisitor().create_map()
        template.add_property('structure1', TemplateMock('Structure'))
        template.add_property('structure2', TemplateMock('Structure'))

        coverage = template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            Coverage(3, 3)
        )

    def test_calculate_coverage_map_half_coverage(self):
        subject = Map({'structure1': StringMock('Structure'), 'structure2': StringMock('Structure')})
        
        template = TemplateFactoryVisitor().create_map()
        template.add_property('structure1', TemplateMock('Structure'))

        coverage = template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            Coverage(3, 2)
        )

    def test_calculate_coverage_map_third_coverage(self):
        subject = Map(
            {
                'structure1': StringMock('Structure'),
                'structure2': StringMock('Structure'),
                'structure3': StringMock('Structure')
            }
        )
        
        template = TemplateFactoryVisitor().create_map()
        template.add_property('structure1', TemplateMock('Structure'))

        coverage = template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            Coverage(4, 2)
        )

    def test_calculate_coverage_map_incompatible(self):
        subject = Map(
            {
                'structure1': StringMock('Structure')
            }
        )
        
        template = TemplateFactoryVisitor().create_map()
        template.add_property('structure1', TemplateMock('Structure'))
        template.add_property('structure2', TemplateMock('Structure'))

        coverage = template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            Coverage(2, 0)
        )

    def test_calculate_coverage_wrong_type(self):
        subject = StringMock()
        
        template = TemplateFactoryVisitor().create_map()
        template.add_property('structure1', TemplateMock('Structure'))
        template.add_property('structure2', TemplateMock('Structure'))

        coverage = template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            Coverage.NOT_COVERED
        )

    def test_can_create_instance(self):
        map_structure = self.map_template.create_instance()
        self.assertIsInstance(map_structure, Map)

    def test_can_get_repr(self):
        representation: str = self.map_template.__repr__()
        self.assertTrue(representation.startswith('MapTemplate('))
