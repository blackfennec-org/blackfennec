# -*- coding: utf-8 -*-
import logging

from src.structure.info import Info
from src.structure.list import List
from src.structure.template.template_base import TemplateBase

logger = logging.getLogger(__name__)


class ListTemplate(TemplateBase, List):
    def __init__(self, subject: List, template_factory, property_storage: dict = None):
        TemplateBase.__init__(self, subject, template_factory, property_storage)

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
                self._template_factory.create(child, self._property_storage)
            )
        return result
    
    def append(self, item: Info):
        """Append item to list template.

        Args:
            item (Info): Item to append.
        """
        decapsulated_item = self._remove_template_class(item)
        self.subject.append(decapsulated_item)

    def remove(self, item: Info):
        """Remove item from List.

        Args:
            item (Info): Item to remove.

        Raises:
            KeyError: If the item passed is not in
                list and hence cannot be removed.
        """
        if self._remove_template_class(item) not in self:
            message = "item not in list"
            logger.error(message)
            raise KeyError(message)
        self.subject.remove(self._remove_template_class(item))

    def __getitem__(self, index):
        item = self.subject[index]
        return self._template_factory.create(item, self._property_storage)

    def __setitem__(self, index, value):
        decapsulated_value = self._remove_template_class(value)
        self.subject[index] = decapsulated_value
        decapsulated_value.parent = self.subject

    def __repr__(self):
        return f'ListTemplate({self.subject.__repr__()})'

    def __contains__(self, item):
        decapsulated_value = self._remove_template_class(item)
        return decapsulated_value in self.subject.data