from src.black_fennec.structure.map import Map
from src.black_fennec.structure.list import List
from src.black_fennec.structure.template.list_template import ListTemplate as Template
from src.black_fennec.structure.template.template_parser import TemplateParser


class ListTemplate(Template):
    """Template of list.

    Class creates Template structure for core type
        list."""

    def __init__(self):
        visitor = TemplateParser()
        Template.__init__(self, visitor, Map({"elements": List()}))

        self._name = 'List'

    @property
    def name(self):
        return self._name
