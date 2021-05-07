from src.structure.encapsulation_base.base_factory_visitor import BaseFactoryVisitor
from src.structure.list import List
from src.structure.map import Map
from src.structure.filter.list_filter import ListFilter
from src.structure.filter.map_filter import MapFilter
from src.structure.filter.filter_base import FilterBase


class FilterFactoryVisitor(BaseFactoryVisitor):
    def __init__(self, metadata_storage: dict = None):
        BaseFactoryVisitor.__init__(self, FilterBase)
        self._metadata_storage = metadata_storage if metadata_storage\
            else dict()

    @property
    def metadata_storage(self):
        return self._metadata_storage

    def visit_map(self, subject_map: Map):
        return MapFilter(self, subject_map)

    def visit_list(self, subject_list: List):
        return ListFilter(self, subject_list)
