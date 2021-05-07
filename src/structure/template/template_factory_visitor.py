from src.structure.encapsulation_base.base_factory_visitor import BaseFactoryVisitor
from src.structure.list import List
from src.structure.map import Map
from src.structure.template.list_template import ListTemplate
from src.structure.template.map_template import MapTemplate
from src.structure.template.template_base import TemplateBase


class TemplateFactoryVisitor(BaseFactoryVisitor):
    def __init__(self, metadata_storage: dict = None):
        BaseFactoryVisitor.__init__(self, TemplateBase)
        self._metadata_storage = metadata_storage if metadata_storage\
            else dict()

    @property
    def metadata_storage(self):
        return self._metadata_storage

    def visit_map(self, subject_map: Map):
        return MapTemplate(self, subject_map)

    def visit_list(self, subject_list: List):
        return ListTemplate(self, subject_list)
