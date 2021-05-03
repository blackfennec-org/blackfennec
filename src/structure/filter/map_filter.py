# -*- coding: utf-8 -*-
from src.structure.map import Map
from src.structure.filter.filter_base import FilterBase


class MapFilter(FilterBase, Map):
    def __init__(
            self,
            subject: Map,
            filter_factory,
            property_storage: dict = None
    ):
        FilterBase.__init__(
            self,
            subject,
            filter_factory,
            property_storage
        )

    @property
    def subject(self) -> Map:
        return self._subject

    @property
    def children(self):
        result = list()
        if not self.subject.children:
            return result
        for child in self.subject.children:
            result.append(
                self._filter_factory.create(
                    child,
                    self._property_storage
                )
            )
        return result

    def __getitem__(self, key):
        item = self.subject[key]
        return self._filter_factory.create(item, self._property_storage)

    def __setitem__(self, key, value):
        decapsulated_value = value
        if isinstance(value, FilterBase):
            base: FilterBase = value
            decapsulated_value = base.subject
        self.subject[key] = decapsulated_value
        decapsulated_value.parent = self.subject

    def __repr__(self):
        return f'MapFilter({self.subject.__repr__()})'
