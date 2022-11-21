import unittest

from blackfennec_doubles.interpretation.double_interpretation import \
    InterpretationMock
from blackfennec_doubles.structure.double_null import NullMock
from core.null.null_view_model import NullViewModel


def test_can_construct():
    NullViewModel(InterpretationMock(NullMock()))


def test_can_get_value():
    null_view_model = NullViewModel(InterpretationMock(NullMock()))
    assert null_view_model.null.value is None


def test_can_set_value():
    null_view_model = NullViewModel(InterpretationMock())
    null_view_model.null = NullMock()
    assert null_view_model.null.value is None
