from doubles.double_dummy import Dummy
from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.structure.double_string import StringMock
from doubles.black_fennec.interpretation.auction.double_coverage import CoverageMock
from src.black_fennec.structure.null import Null

from src.black_fennec.structure.type.type import Type


class TypeMock(Type):
    def __init__(self, type=None, coverage=None, default=None, super_type=None):
        if super_type:
            super_structure = super_type.subject
        else:
            super_structure = Null()
        super().__init__(
            MapMock({"type": StringMock("String"), "super": super_structure})
        )
        self.type = type
        self._coverage = coverage or CoverageMock(1)
        self._default = default or StringMock("Default")

    @property
    def default(self):
        return self._default

    def calculate_coverage(self, subject):
        return self._coverage

    def __repr__(self):
        return f"TypeMock({self.type})"
