from src.black_fennec.structure.map import Map
from src.black_fennec.structure.template.map_template import MapTemplate as Template
from src.black_fennec.structure.template.template_factory_visitor import TemplateFactoryVisitor


class MapTemplate(Template):
    """Template of map.

    Class creates Template structure for core type
        map."""

    def __init__(self):
        visitor = TemplateFactoryVisitor()
        Template.__init__(self, visitor, Map())
