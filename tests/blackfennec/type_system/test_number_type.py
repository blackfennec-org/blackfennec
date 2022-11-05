import pytest

from blackfennec.structure.number import Number
from blackfennec.structure.map import Map
from blackfennec.type_system.number_type import NumberType
from blackfennec.type_system.type_factory import TypeFactory
from blackfennec.interpretation.auction.coverage import Coverage


class TestNumberType:
    @pytest.fixture
    def type(self) -> NumberType:
        return TypeFactory().create_number()

    def test_can_be_created(self, type):
        ...

    def test_omitted_default(self):
        type = NumberType(Map())
        assert type.default.value == Number().value
    
    def test_omitted_maximum(self):
        type = NumberType(Map())
        assert type.maximum == None

    def test_omitted_minimum(self):
        type = NumberType(Map())
        assert type.minimum == None

    def test_default(self, type: NumberType):
        assert type.default.value == Number().value

    def test_minimum_default(self, type: NumberType):
        assert type.minimum == None

    def test_set_minimum(self, type: NumberType):
        type.minimum = -1337
        assert type.minimum == -1337
    
    def test_maximum_default(self, type: NumberType):
        assert type.maximum == None

    def test_set_maximum(self, type: NumberType):
        type.maximum = 1337
        assert type.maximum == 1337

    def test_visitor(self, type: NumberType):
        structure = Number()
        coverage = type.visit_number(structure)
        assert coverage == Coverage.COVERED

    def test_visitor_checks_minimum(self, type: NumberType):
        structure = Number(10)
        type.minimum = 15
        coverage = type.visit_number(structure)
        assert coverage == Coverage.NOT_COVERED

    def test_visitor_checks_maximum(self, type: NumberType):
        structure = Number(20)
        type.maximum = 15
        coverage = type.visit_number(structure)
        assert coverage == Coverage.NOT_COVERED

    def test_visitor_allows_exactly(self, type: NumberType):
        structure = Number(15)
        type.minimum = 15
        type.maximum = 15
        coverage = type.visit_number(structure)
        assert coverage == Coverage.COVERED

    def test_can_reset_limits(self, type: NumberType):
        structure = Number(15)
        type.minimum = 0
        type.maximum = 0
        type.minimum = 15
        type.maximum = 15
        coverage = type.visit_number(structure)
        assert coverage == Coverage.COVERED

    def test_can_get_repr(self, type):
        representation: str = str(type)
        assert representation.startswith("NumberType(")
