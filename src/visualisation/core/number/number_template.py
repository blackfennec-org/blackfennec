from src.black_fennec.structure.map import Map
from src.black_fennec.structure.template.number_template import NumberTemplate as Template
from src.black_fennec.structure.template.template_parser import TemplateParser


class NumberTemplate(Template):
    """Template of number.

    Class creates Template structure for core type
        number."""

    def __init__(self):
        visitor = TemplateParser()
        Template.__init__(self, visitor, Map())

        self._name = 'Number'

    @property
    def name(self):
        return self._name
