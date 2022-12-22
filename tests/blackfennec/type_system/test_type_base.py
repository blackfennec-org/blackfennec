# -*- coding: utf-8 -*-
import pytest

from tests.test_utils.parameterize import CORE_STRUCTURES, CORE_TYPES
from blackfennec_doubles.structure.double_structure import StructureMock
from blackfennec.structure.structure import Structure
from blackfennec.type_system.type import Type
from blackfennec.type_system.type_factory import TypeFactory
from blackfennec.type_system.interpretation.coverage import Coverage


@pytest.fixture
def type(request):
    parent = TypeFactory.create_map()
    type = request.param()
    parent.add_property('child', type)
    return type


@pytest.mark.parametrize("type", CORE_TYPES, indirect=True)
def test_can_construct(type):
    assert type is not None


@pytest.mark.parametrize("type", CORE_TYPES, indirect=True)
def test_optional_getter(type):
    assert type.is_optional == False


@pytest.mark.parametrize("type", CORE_TYPES, indirect=True)
def test_optional_setter(type):
    type.is_optional = True
    assert type.is_optional == True


@pytest.mark.parametrize(["type", "structure"], zip(CORE_TYPES, CORE_STRUCTURES), indirect=["type"])
def test_can_calculate_coverage_of_structure(type, structure):
    coverage = type.calculate_coverage(structure)
    assert coverage == Coverage.COVERED


@pytest.mark.parametrize("type", CORE_TYPES, indirect=True)
def test_has_create_instance_interface(type):
    instance = type.create_instance()
    assert isinstance(instance, Structure)
