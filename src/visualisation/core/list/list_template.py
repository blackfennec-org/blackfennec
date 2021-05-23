from src.black_fennec.structure.list import List
from src.black_fennec.structure.template.list_template import ListTemplate as Template
from src.black_fennec.structure.template.template_factory_visitor import TemplateFactoryVisitor


class ListTemplate(Template):
    """Template of list.

    Class creates Template structure for core type
        list."""

    def __init__(self):
        visitor = TemplateFactoryVisitor()
        Template.__init__(self, visitor, List())
