# -*- coding: utf-8 -*-
import logging

from src.structure.info import Info
from src.structure.list import List
from src.structure.filter.filter_base import FilterBase

logger = logging.getLogger(__name__)


class ListFilter(FilterBase, List):
    def __init__(
            self,
            subject: List,
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
    def subject(self) -> List:
        return self._subject

    @property
    def children(self):
        result = list()
        if not self.subject.children:
            return result
        for child in self.subject.children:
            result.append(
                self._filter_factory.create(child, self._property_storage)
            )
        return result
    
    def append(self, item: Info):
        """Append item to list filter.

        Args:
            item (Info): Item to append.
        """
        decapsulated_item = self._remove_filter_class(item)
        self.subject.append(decapsulated_item)

    def remove(self, item: Info):
        """Remove item from List.

        Args:
            item (Info): Item to remove.

        Raises:
            KeyError: If the item passed is not in
                list and hence cannot be removed.
        """
        decapsulated_value = self._remove_filter_class(item)
        if decapsulated_value not in self:
            message = 'item not in list'
            logger.error(message)
            raise KeyError(message)
        self.subject.remove(decapsulated_value)

    def __getitem__(self, index):
        item = self.subject[index]
        return self._filter_factory.create(item, self._property_storage)

    def __setitem__(self, index, value):
        decapsulated_value = self._remove_filter_class(value)
        self.subject[index] = decapsulated_value
        decapsulated_value.parent = self.subject

    def __contains__(self, item):
        decapsulated_value = self._remove_filter_class(item)
        return decapsulated_value in self.subject

    def __repr__(self):
        return f'ListFilter({self.subject.__repr__()})'
