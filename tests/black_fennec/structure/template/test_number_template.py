import pytest

from src.black_fennec.structure.number import Number
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.template.number_template import NumberTemplate
from src.black_fennec.structure.template.template_factory import TemplateFactory
from src.black_fennec.interpretation.auction.coverage import Coverage


class TestNumberTemplate:
    @pytest.fixture
    def template(self) -> NumberTemplate:
        return TemplateFactory().create_number()

    def test_can_be_created(self, template):
        ...

    def test_omitted_default(self):
        template = NumberTemplate(None, Map())
        assert template.default.value == Number().value
    
    def test_omitted_maximum(self):
        template = NumberTemplate(None, Map())
        assert template.maximum == None

    def test_omitted_minimum(self):
        template = NumberTemplate(None, Map())
        assert template.minimum == None

    def test_default(self, template: NumberTemplate):
        assert template.default.value == Number().value

    def test_minimum_default(self, template: NumberTemplate):
        assert template.minimum == None

    def test_set_minimum(self, template: NumberTemplate):
        template.minimum = -1337
        assert template.minimum == -1337
    
    def test_maximum_default(self, template: NumberTemplate):
        assert template.maximum == None

    def test_set_maximum(self, template: NumberTemplate):
        template.maximum = 1337
        assert template.maximum == 1337

    def test_visitor(self, template: NumberTemplate):
        structure = Number()
        coverage = template.visit_number(structure)
        assert coverage == Coverage.COVERED

    def test_visitor_checks_minimum(self, template: NumberTemplate):
        structure = Number(10)
        template.minimum = 15
        coverage = template.visit_number(structure)
        assert coverage == Coverage.NOT_COVERED

    def test_visitor_checks_maximum(self, template: NumberTemplate):
        structure = Number(20)
        template.maximum = 15
        coverage = template.visit_number(structure)
        assert coverage == Coverage.NOT_COVERED

    def test_visitor_allows_exactly(self, template: NumberTemplate):
        structure = Number(15)
        template.minimum = 15
        template.maximum = 15
        coverage = template.visit_number(structure)
        assert coverage == Coverage.COVERED
    
    @pytest.mark.xfail
    def test_can_reset_limits(self, template: NumberTemplate):
        structure = Number(15)
        template.minimum = 0
        template.maximum = 0
        template.minimum = 15
        template.maximum = 15
        coverage = template.visit_number(structure)
        assert coverage == Coverage.COVERE

    def test_can_get_repr(self, template):
        representation: str = str(template)
        assert representation.startswith("NumberTemplate(")
