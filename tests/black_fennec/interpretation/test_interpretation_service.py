# -*- coding: utf-8 -*-

import pytest

from doubles.black_fennec.interpretation.auction.double_auctioneer import AuctioneerMock
from doubles.visualisation.double_structure_view_factory import StructureViewFactoryMock
from doubles.double_dummy import Dummy
from doubles.black_fennec.type_system.double_type_registry import TypeRegistryMock
from doubles.black_fennec.structure.type.double_type import TypeMock
from src.black_fennec.interpretation.interpretation import Interpretation
from src.black_fennec.interpretation.interpretation_service import InterpretationService

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
