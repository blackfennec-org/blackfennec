from src.black_fennec.structure.boolean import Boolean
from src.black_fennec.structure.template.template_base import TemplateBase
from src.black_fennec.structure.template.template_factory_visitor import TemplateFactoryVisitor


class BooleanTemplate(TemplateBase):
    """Template of boolean.

    Class creates Template structure for core type
        boolean."""

    def __init__(self):
        visitor = TemplateFactoryVisitor()
        TemplateBase.__init__(self, visitor, Boolean())

        self._name = "Boolean"

    @property
    def name(self):
        return self._name
