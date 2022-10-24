# -*- coding: utf-8 -*-

from blackfennec.structure.visitor import Visitor
from blackfennec.structure.encapsulation_base.base_factory_visitor import BaseFactoryVisitor
from blackfennec.structure.list import List
from blackfennec.structure.map import Map
from blackfennec.structure.filter.list_filter import ListFilter
from blackfennec.structure.filter.map_filter import MapFilter
from blackfennec.structure.filter.filter_base import FilterBase


class FilterFactoryVisitor(BaseFactoryVisitor):
    """Filter Factory Visitor

    Class is a concrete factory which produces Filter based
        structure encapsulations. Only few methods are overwritten
        which require specialised functionality. For all other
        structure types the abstract factory implementation suffices.
    """

    def __init__(self, metadata_storage: dict = None):
        BaseFactoryVisitor.__init__(self, FilterBase)
        self._metadata_storage = metadata_storage if metadata_storage \
            else {}

    @property
    def metadata_storage(self):
        """Metadata storage getter.

        Is used to keep track of the decoration attributes for
            the respecting encapsulated structure. The structure functions
            as key in the dictionary.

        Returns:
             dict: dictionary containing values that belong to
                a specific encapsulated structure, which is used as
                key in the dictionary.
        """
        return self._metadata_storage

    def visit_map(self, subject_map: Map) -> MapFilter:
        return MapFilter(self, subject_map)

    def visit_list(self, subject_list: List) -> ListFilter:
        return ListFilter(self, subject_list)
