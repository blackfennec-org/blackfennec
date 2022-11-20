import pytest

from blackfennec.layers.encapsulation_base.reference_encapsulation_base import \
    ReferenceEncapsulationBase
from blackfennec_doubles.layers.encapsulation_base.double_factory_base_visitor import \
    FactoryBaseVisitorMock
from blackfennec_doubles.structure.double_reference import ReferenceMock
from blackfennec_doubles.structure.double_string import StringMock


@pytest.fixture
def visitor():
    return FactoryBaseVisitorMock()


def test_can_resolve(visitor):
    subject = ReferenceMock(resolve_return=StringMock('test'))
    reference_encapsulation_base = ReferenceEncapsulationBase(
        visitor,
        subject
    )
    reference_encapsulation_base.resolve()
    assert subject.resolve_count == 1
    assert visitor.visit_string_count == 1
