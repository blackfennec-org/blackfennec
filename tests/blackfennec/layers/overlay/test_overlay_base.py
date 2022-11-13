# -*- coding: utf-8 -*-
import pytest

from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec_doubles.layers.encapsulation_base.double_factory_base_visitor import FactoryBaseVisitorMock
from blackfennec_doubles.double_dummy import Dummy
from blackfennec.layers.overlay.overlay_base import OverlayBase
from blackfennec.util.parameterized_visitor import ParameterizedVisitor


@pytest.fixture
def overlay_base():
    visitor = FactoryBaseVisitorMock()
    parent = Dummy('parent')
    root = Dummy('root')
    subject = StructureMock(parent=parent, root=root)
    return OverlayBase(visitor, subject)

def test_can_construct(overlay_base):
    assert overlay_base is not None

def test_can_accept_and_return_self(overlay_base):
    return_self = ParameterizedVisitor(default=lambda s: s)
    self = overlay_base.accept(return_self)
    assert self is overlay_base

def test_can_get_repr(overlay_base):
    representation: str = overlay_base.__repr__()
    assert representation.startswith('OverlayBase(')
