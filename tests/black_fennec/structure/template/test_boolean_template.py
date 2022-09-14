import pytest

from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.template.boolean_template import BooleanTemplate
from src.black_fennec.structure.template.template_factory import TemplateFactory
from src.black_fennec.interpretation.auction.coverage import Coverage


class TestBooleanTemplate:
    @pytest.fixture
    def template(self) -> BooleanTemplate:
        return TemplateFactory().create_boolean()

    def test_can_construct(self, template):
        ...

    def test_default(self, template: BooleanTemplate):
        assert template.default.value == Boolean().value

    def test_omitted_default(self):
        template = BooleanTemplate(None, Map())
        assert template.default.value == Boolean().value

    def test_minimum_default(self, template: BooleanTemplate):
        assert template.expected == None

    def test_set_expected_to_true(self, template: BooleanTemplate):
        template.expected = True
        assert template.expected == True

    def test_reuses_structure_for_expected(self, template):
        template.expected = True
        structure = template.value['expected']
        template.expected = False
        assert structure is template.value['expected']
    
    def test_set_expected_to_false(self, template: BooleanTemplate):
        template.expected = False
        assert template.expected == False

    def test_visitor(self, template: BooleanTemplate):
        structure = Boolean()
        coverage = template.visit_boolean(structure)
        assert coverage == Coverage.COVERED

    def test_visitor_expected_true(self, template: BooleanTemplate):
        structure = Boolean(True)
        template.expected = True
        coverage = template.visit_boolean(structure)
        assert coverage == Coverage.COVERED

    def test_visitor_expected_false(self, template: BooleanTemplate):
        structure = Boolean(True)
        template.expected = False
        coverage = template.visit_boolean(structure)
        assert coverage == Coverage.NOT_COVERED

    def test_repr(self, template: BooleanTemplate):
        assert 'BooleanTemplate' in str(template)
