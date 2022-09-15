from src.black_fennec.structure.string import String
from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.number import Number
from src.black_fennec.structure.map import Map
from src.black_fennec.structure.list import List
from src.black_fennec.structure.boolean import Boolean
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
    Reference(Dummy()),
    String(), Number(), Boolean()
]