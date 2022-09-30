from src.black_fennec.structure.reference import Reference
from src.black_fennec.structure.template.template_base import TemplateBase
from src.black_fennec.structure.template.template_factory_visitor import TemplateFactoryVisitor


class ReferenceTemplate(TemplateBase):
    """Template of reference.

    Class creates Template structure for core type
        reference."""

    def __init__(self):
        visitor = TemplateFactoryVisitor()
        TemplateBase.__init__(self, visitor, Reference([]))

        self._name = 'Reference'

    @property
    def name(self):
        return self._name
