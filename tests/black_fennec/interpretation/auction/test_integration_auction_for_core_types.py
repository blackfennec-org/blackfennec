import pytest

from doubles.double_dummy import Dummy
from src.black_fennec.interpretation.auction.auctioneer import Auctioneer
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.type.boolean_type import BooleanType
from src.black_fennec.structure.list import List
from src.black_fennec.structure.type.list_type import ListType
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.type.map_type import MapType
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.type.number_type import NumberType
from src.black_fennec.structure.string import String
from src.black_fennec.structure.type.string_type import StringType
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.type.reference_type import ReferenceType
from src.black_fennec.structure.null import Null
from src.black_fennec.structure.type.null_type import NullType

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
