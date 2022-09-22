from doubles.double_dummy import Dummy
from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.structure.double_string import StringMock

from src.black_fennec.structure.type.type import Type


class TypeMock(Type):
    def __init__(self, type):
        super().__init__(
            MapMock({"type": StringMock("String")})
        )
        self.type = type

    @property
    def default(self):
        return StringMock("Default")

    def __repr__(self):
        return f"TypeMock({self.type})"
