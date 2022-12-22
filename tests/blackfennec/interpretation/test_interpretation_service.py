# -*- coding: utf-8 -*-

import pytest

from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.type_system.double_type_registry import TypeRegistryMock
from blackfennec_doubles.type_system.double_type import TypeMock
from blackfennec_doubles.type_system.interpretation.double_specification import SpecificationMock
from blackfennec_doubles.type_system.interpretation.double_coverage import CoverageMock
from blackfennec.type_system.interpretation.interpretation_service import InterpretationService


@pytest.fixture
def type_registry():
    type0 = TypeMock(coverage=CoverageMock(1))
    type1 = TypeMock(coverage=CoverageMock(0.5))
    type2 = TypeMock(coverage=CoverageMock(0))
    return TypeRegistryMock([type0, type1, type2])

@pytest.fixture
def interpreter(type_registry):
    interpreter = InterpretationService(type_registry)
    return interpreter

def test_create_interpreter(interpreter):
    assert interpreter is not None

def test_can_create_interpretation(interpreter, type_registry):
    structure = Dummy("structure")
    interpretation = interpreter.interpret(structure, SpecificationMock())
    assert type_registry.types[0] is interpretation.types[0]

def test_all_satisfying_offers_are_returned(interpreter, type_registry):
    structure = Dummy("structure")
    interpretation = interpreter.interpret(structure, SpecificationMock())
    assert type_registry.types[1] is interpretation.types[1]

def test_only_satisfying_offers_are_considered(interpreter, type_registry):
    subject = Dummy('Structure')
    interpretation = interpreter.interpret(subject, SpecificationMock())
    assert type_registry.types[2] not in interpretation.types

def test_auction_with_no_fitting_offers():
    interpreter = InterpretationService(TypeRegistryMock([]))
    subject = Dummy('Structure')
    interpretation = interpreter.interpret(subject, SpecificationMock())
    assert interpretation.types == []
