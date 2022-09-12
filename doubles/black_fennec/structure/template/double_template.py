from doubles.double_dummy import Dummy
from doubles.black_fennec.structure.double_map import MapMock
from doubles.black_fennec.structure.double_string import StringMock

from src.black_fennec.structure.template.template import Template


class TemplateMock(Template):
    def __init__(self, type):
        super().__init__(
            Dummy("Visitor"), MapMock({"type": StringMock("String")})
        )
        self.type = type

    @property
    def default(self):
        return StringMock("Default")

    def __repr__(self):
        return f"TemplateMock({self.type})"
