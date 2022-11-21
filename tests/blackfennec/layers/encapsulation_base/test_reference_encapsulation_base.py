import pytest

from blackfennec.layers.encapsulation_base.reference_encapsulation_base import \
    ReferenceEncapsulationBase
from blackfennec_doubles.layers.double_layer import LayerMock
from blackfennec_doubles.structure.double_reference import ReferenceMock
from blackfennec_doubles.structure.double_string import StringMock


@pytest.fixture
def layer():
    return LayerMock()


def test_can_resolve(layer):
    target = StringMock('test')
    subject = ReferenceMock(resolve_return=target)
    reference_encapsulation_base = ReferenceEncapsulationBase(
        layer=layer,
        subject=subject
    )
    reference_encapsulation_base.resolve()
    assert subject.resolve_count == 1
    assert layer.get_stats(target)[0] == 1
