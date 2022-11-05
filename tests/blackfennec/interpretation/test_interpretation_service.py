# -*- coding: utf-8 -*-

import pytest

from blackfennec_doubles.interpretation.auction.double_auctioneer import AuctioneerMock
from blackfennec_doubles.extension.double_structure_view_factory import StructureViewFactoryMock
from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.type_system.double_type_registry import TypeRegistryMock
from blackfennec_doubles.type_system.double_type import TypeMock
from blackfennec.interpretation.interpretation import Interpretation
from blackfennec.interpretation.interpretation_service import InterpretationService

@pytest.fixture
def type_registry():
    types = [TypeMock()]
    return TypeRegistryMock(types)

@pytest.fixture
def interpreter(type_registry):
    interpreter = InterpretationService(type_registry)
    return interpreter

def test_create_interpreter(interpreter):
    assert interpreter is not None

def test_can_create_interpretation(interpreter, type_registry):
    structure = Dummy("structure")
    interpretation = interpreter.interpret(structure)
    assert type_registry.types[0] in interpretation.types
