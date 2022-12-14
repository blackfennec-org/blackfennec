import pytest

from blackfennec_doubles.double_dummy import Dummy
from blackfennec_doubles.type_system.double_type_registry import TypeRegistryMock
from blackfennec_doubles.type_system.interpretation.double_specification import SpecificationMock
from blackfennec.type_system.interpretation.interpretation_service import InterpretationService
from blackfennec.structure.boolean import Boolean
from blackfennec.type_system.boolean_type import BooleanType
from blackfennec.structure.list import List
from blackfennec.type_system.list_type import ListType
from blackfennec.structure.map import Map
from blackfennec.type_system.map_type import MapType
from blackfennec.structure.number import Number
from blackfennec.type_system.number_type import NumberType
from blackfennec.structure.string import String
from blackfennec.type_system.string_type import StringType
from blackfennec.structure.reference import Reference
from blackfennec.type_system.reference_type import ReferenceType
from blackfennec.structure.null import Null
from blackfennec.type_system.null_type import NullType

pytestmark = pytest.mark.integration

@pytest.fixture
def types():
    types = [
        BooleanType(),
        NumberType(),
        StringType(),
        ListType(),
        MapType(),
        ReferenceType(),
        NullType()
    ]
    return types


@pytest.mark.parametrize(
    ["structure", "type"],
    [
        (Map(), MapType),
        (List(), ListType),
        (Reference(Dummy()), ReferenceType),
        (String(), StringType),
        (Number(), NumberType),
        (Boolean(), BooleanType),
        (Null(), NullType)
    ],
    ids=[
        "map",
        "list",
        "reference",
        "string",
        "number",
        "boolean",
        "null"
    ])
def test_auction(types, structure, type):
    service = InterpretationService(TypeRegistryMock(types))
    interpretation = service.interpret(structure, SpecificationMock())
    interpreted_types = interpretation.types
    assert isinstance(interpreted_types[0], type)
