from src.black_fennec.structure.map import Map
from src.black_fennec.structure.string import String
from src.black_fennec.structure.template.string_template import StringTemplate as Template
from src.black_fennec.structure.template.template_parser import TemplateParser


class StringTemplate(Template):
    """Template of string.

    Class creates Template structure for core type
        string."""

    def __init__(self):
        visitor = TemplateParser()
        Template.__init__(self, visitor, Map())
        self._name = 'String'

    @property
    def name(self):
        return self._name
