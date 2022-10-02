import pytest

from src.black_fennec.structure.null import Null
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.type.null_type import NullType
from src.black_fennec.structure.type.type_factory import TypeFactory
from src.black_fennec.interpretation.auction.coverage import Coverage


@pytest.fixture
def type() -> NullType:
    return TypeFactory().create_null()

def test_can_construct(type):
    assert type.subject.value["type"].value == "Null"

def test_default(type: NullType):
    assert type.default.value == Null().value


def test_visitor(type: NullType):
    structure = Null()
    coverage = type.visit_null(structure)
    assert coverage == Coverage.COVERED

def test_repr(type: NullType):
    assert 'NullType' in str(type)
