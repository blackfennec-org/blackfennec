from src.black_fennec.structure.string import String
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.list import List
from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.null import Null
from src.black_fennec.structure.type.string_type import StringType
from src.black_fennec.structure.type.reference_type import ReferenceType
from src.black_fennec.structure.type.null_type import NullType
from src.black_fennec.structure.type.number_type import NumberType
from src.black_fennec.structure.type.map_type import MapType
from src.black_fennec.structure.type.list_type import ListType
from src.black_fennec.structure.type.boolean_type import BooleanType
from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.double_list import ListMock
from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.structure.double_number import NumberMock
from doubles.black_fennec.structure.double_reference import ReferenceMock
from doubles.black_fennec.structure.double_string import StringMock
from doubles.black_fennec.structure.double_boolean import BooleanMock
from doubles.double_dummy import Dummy


MOCK_CORE_TYPES = [
    MapMock(), ListMock(),
    StringMock(), NumberMock(), BooleanMock(),
    ReferenceMock()
]

CORE_TYPES = [
    Map(), List(),
    Reference(Dummy()), Null(),
    String(), Number(), Boolean()
]

CORE_TTYPES = [
    MapType,
    ListType,
    ReferenceType,
    NullType,
    StringType,
    NumberType,
    BooleanType
]

CORE_TYPE_FACTORIES = {
    "argnames": "create_structure",
    "argvalues": [
        lambda: Map(),
        lambda: List(),
        lambda: Reference(Dummy()),
        lambda: String(),
        lambda: Number(),
        lambda: Boolean(),
        lambda: Null()
    ],
    "ids": [
        "map",
        "list",
        "reference",
        "string",
        "number",
        "boolean",
        "null"
    ]
}