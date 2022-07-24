from doubles.double_dummy import Dummy
from doubles.black_fennec.structure.double_structure import StructureMock
from doubles.black_fennec.structure.double_string import StringMock

from src.black_fennec.structure.template.template_base import TemplateBase

class TemplateMock(TemplateBase):
    def __init__(self, type):
        super().__init__(Dummy('Visitor'), StructureMock({'type': StringMock('String')}))
        self.type = type

    def __repr__(self):
        return f'TemplateMock({self.type})'