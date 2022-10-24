import pytest

from blackfennec_doubles.double_dummy import Dummy
from blackfennec.interpretation.auction.auctioneer import Auctioneer
from blackfennec.structure.boolean import Boolean
from blackfennec.structure.type.boolean_type import BooleanType
from blackfennec.structure.list import List
from blackfennec.structure.type.list_type import ListType
from blackfennec.structure.map import Map
from blackfennec.structure.type.map_type import MapType
from blackfennec.structure.number import Number
from blackfennec.structure.type.number_type import NumberType
from blackfennec.structure.string import String
from blackfennec.structure.type.string_type import StringType
from blackfennec.structure.reference import Reference
from blackfennec.structure.type.reference_type import ReferenceType
from blackfennec.structure.null import Null
from blackfennec.structure.type.null_type import NullType

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
    result = Auctioneer.auction(types, structure)
    assert isinstance(result[0], type)
