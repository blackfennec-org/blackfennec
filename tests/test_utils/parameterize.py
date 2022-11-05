from blackfennec_doubles.structure.double_boolean import BooleanMock
from blackfennec_doubles.structure.double_list import ListMock
from blackfennec_doubles.structure.double_map import MapMock
from blackfennec_doubles.structure.double_number import NumberMock
from blackfennec_doubles.structure.double_reference import ReferenceMock
from blackfennec_doubles.structure.double_string import StringMock
from blackfennec.structure.boolean import Boolean
from blackfennec.structure.list import List
from blackfennec.structure.map import Map
from blackfennec.structure.null import Null
from blackfennec.structure.number import Number
from blackfennec.structure.reference import Reference
from blackfennec.structure.string import String
from blackfennec.type_system.boolean_type import BooleanType
from blackfennec.type_system.list_type import ListType
from blackfennec.type_system.map_type import MapType
from blackfennec.type_system.null_type import NullType
from blackfennec.type_system.number_type import NumberType
from blackfennec.type_system.reference_type import ReferenceType
from blackfennec.type_system.string_type import StringType

MOCK_CORE_STRUCTURES = [
    MapMock(), ListMock(),
    StringMock(), NumberMock(), BooleanMock(),
    ReferenceMock()
]

CORE_STRUCTURES = [
    Map(), List(),
    Reference([]), Null(),
    String(), Number(), Boolean()
]

CORE_TYPES = [
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
        lambda: Reference([]),
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
