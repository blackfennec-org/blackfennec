import pytest

from blackfennec_doubles.interpretation.double_interpretation import \
    InterpretationMock
from blackfennec_doubles.structure.double_null import NullMock
from blackfennec.interpretation.specification import Specification
from core.null.null_preview import NullPreview
from core.null.null_view_factory import NullViewFactory


@pytest.fixture
def factory():
    return NullViewFactory()


def test_can_construct(factory):
    assert factory is not None


def test_can_create_null_preview(factory):
    specification = Specification(request_preview=True)
    view = factory.create(
        InterpretationMock(NullMock(),
                           specification=specification))
    assert isinstance(view, NullPreview)


def test_does_not_satisfy_default(factory):
    satisfies = factory.satisfies(Specification())
    assert not satisfies


def test_does_satisfy_preview(factory):
    satisfies = factory.satisfies(Specification(request_preview=True))
    assert satisfies
