from src.black_fennec.structure.string import String
from src.black_fennec.structure.template.string_template import StringTemplate as Template
from src.black_fennec.structure.template.template_factory_visitor import TemplateFactoryVisitor


class StringTemplate(Template):
    """Template of string.

    Class creates Template structure for core type
        string."""

    def __init__(self):
        visitor = TemplateFactoryVisitor()
        Template.__init__(self, visitor, String())
        self._name = 'String'

    @property
    def name(self):
        return self._name
