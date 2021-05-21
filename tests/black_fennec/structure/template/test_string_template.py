import unittest

from doubles.black_fennec.structure.double_info import InfoMock
from doubles.black_fennec.structure.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from src.black_fennec.interpretation.auction.coverage import Coverage
from src.black_fennec.structure.root import Root
from src.black_fennec.structure.string import String
from src.black_fennec.structure.template.string_template import StringTemplate
from src.black_fennec.structure.template.template_base import TemplateBase


class ListTemplateTestSuite(unittest.TestCase):
    def setUp(self):
        self.visitor = FactoryBaseVisitorMock()
        self.subject = String()
        self.subject.parent = Root(self.subject)
        self.string_template = StringTemplate(self.visitor, self.subject)

    def tearDown(self) -> None:
        self.visitor = None
        self.subject = None
        self.string_template = None

    def test_can_construct(self):
        pass

    def test_can_calculate_coverage(self):
        coverage = self.string_template.calculate_coverage(self.subject)
        self.assertEqual(
            coverage,
            Coverage.COVERED
        )

    def test_can_calculate_coverage_pattern_match(self):
        template = String('[a-z]')
        string_template = StringTemplate(self.visitor, template)
        subject = String('a')
        coverage = string_template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            Coverage.COVERED
        )

    def test_can_calculate_coverage_normal_string(self):
        template = String('Test')
        string_template = StringTemplate(self.visitor, template)
        subject = String('Test123')
        coverage = string_template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            Coverage.COVERED
        )

    def test_can_calculate_coverage_pattern_mismatch(self):
        template = String('[a-z]')
        string_template = StringTemplate(self.visitor, template)
        subject = String('A')
        coverage = string_template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            Coverage.NOT_COVERED
        )

    def test_calculate_coverage_wrong_type(self):
        subject = InfoMock()

        coverage = self.string_template.calculate_coverage(subject)
        self.assertEqual(
            coverage,
            Coverage.NOT_COVERED
        )

    def test_can_get_repr(self):
        representation: str = self.string_template.__repr__()
        self.assertTrue(representation.startswith('StringTemplate('))