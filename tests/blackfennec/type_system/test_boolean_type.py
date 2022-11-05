import pytest

from blackfennec.structure.boolean import Boolean
from blackfennec.structure.map import Map
from blackfennec.type_system.boolean_type import BooleanType
from blackfennec.type_system.type_factory import TypeFactory
from blackfennec.interpretation.auction.coverage import Coverage


class TestBooleanType:
    @pytest.fixture
    def type(self) -> BooleanType:
        return TypeFactory().create_boolean()

    def test_can_construct(self, type):
        ...

    def test_default(self, type: BooleanType):
        assert type.default.value == Boolean().value

    def test_omitted_default(self):
        type = BooleanType(Map())
        assert type.default.value == Boolean().value

    def test_minimum_default(self, type: BooleanType):
        assert type.expected == None

    def test_set_expected_to_true(self, type: BooleanType):
        type.expected = True
        assert type.expected == True

    def test_reuses_structure_for_expected(self, type):
        type.expected = True
        structure = type.subject.value['expected']
        type.expected = False
        assert structure is type.subject.value['expected']
    
    def test_set_expected_to_false(self, type: BooleanType):
        type.expected = False
        assert type.expected == False

    def test_visitor(self, type: BooleanType):
        structure = Boolean()
        coverage = type.visit_boolean(structure)
        assert coverage == Coverage.COVERED

    def test_visitor_expected_true(self, type: BooleanType):
        structure = Boolean(True)
        type.expected = True
        coverage = type.visit_boolean(structure)
        assert coverage == Coverage.COVERED

    def test_visitor_expected_false(self, type: BooleanType):
        structure = Boolean(True)
        type.expected = False
        coverage = type.visit_boolean(structure)
        assert coverage == Coverage.NOT_COVERED

    def test_repr(self, type: BooleanType):
        assert 'BooleanType' in str(type)
