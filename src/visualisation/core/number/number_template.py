from src.black_fennec.structure.number import Number
from src.black_fennec.structure.template.template_base import TemplateBase
from src.black_fennec.structure.template.template_factory_visitor import TemplateFactoryVisitor


class NumberTemplate(TemplateBase):
    """Template of number.

    Class creates Template structure for core type
        number."""

    def __init__(self):
        visitor = TemplateFactoryVisitor()
        TemplateBase.__init__(self, visitor, Number())

        self._name = 'Number'

    @property
    def name(self):
        return self._name
