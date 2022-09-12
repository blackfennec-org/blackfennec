from src.black_fennec.structure.map import Map
from src.black_fennec.structure.template.boolean_template import BooleanTemplate as Template
from src.black_fennec.structure.template.template_parser import TemplateParser


class BooleanTemplate(Template):
    """Template of boolean.

    Class creates Template structure for core type
        boolean."""

    def __init__(self):
        visitor = TemplateParser()
        Template.__init__(self, visitor, Map())

        self._name = "Boolean"

    @property
    def name(self):
        return self._name
