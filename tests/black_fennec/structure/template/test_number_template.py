import pytest

from src.black_fennec.structure.number import Number
from src.black_fennec.structure.template.number_template import NumberTemplate
from src.black_fennec.structure.template.template_factory import TemplateFactory


class TestNumberTemplate:
    @pytest.fixture
    def template(self) -> NumberTemplate:
        return TemplateFactory().create_number()

    def test_can_construct(self, template):
        ...

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
