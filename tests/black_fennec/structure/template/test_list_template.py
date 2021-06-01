import unittest

from doubles.black_fennec.structure.double_structure import StructureMock
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.list import List
from src.black_fennec.structure.root import Root
from src.black_fennec.structure.string import String
from src.black_fennec.structure.template.list_template import ListTemplate
from src.black_fennec.structure.template.template_factory_visitor import TemplateFactoryVisitor


class ListTemplateTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = TemplateFactoryVisitor()
        self.subject = List()
        self.subject.parent = Root(self.subject)
        self.list_template = ListTemplate(self.visitor, self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.list_template = None

    def test_can_construct(self):
        pass

    def test_coverage_getter_list_full_coverage(self):
        subject = List([StructureMock('Structure1'), StructureMock('Structure2')])
        template = List([StructureMock('Structure')])
        list_template = ListTemplate(self.visitor, template)

        coverage = list_template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            Coverage(3, 3)
        )

    def test_coverage_getter_list_half_coverage(self):
        subject = List([StructureMock('Structure1'), String('Structure2')])
        template = List([StructureMock('Structure')])
        list_template = ListTemplate(self.visitor, template)

        coverage = list_template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            Coverage(3, 2)
        )

    def test_calculate_coverage_wrong_type(self):
        subject = StructureMock()

        coverage = self.list_template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            Coverage.NOT_COVERED
        )

    def test_can_create_structure(self):
        list_structure = self.list_template.create_structure()
        self.assertIsInstance(list_structure, List)

    def test_can_get_repr(self):
        representation: str = self.list_template.__repr__()
        self.assertTrue(representation.startswith('ListTemplate('))
