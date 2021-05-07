# -*- coding: utf-8 -*-
import logging

from src.structure.encapsulation_base.encapsulation_base import EncapsulationBase
from src.structure.info import Info
from src.structure.list import List

logger = logging.getLogger(__name__)


class ListEncapsulationBase(EncapsulationBase, List):
    """Base Class for ecapsulations of a List.

    Contains List specific overrides of certain functions
        to ensure the encapsulation of any Info returned
        in order to stay in the encapsulation layer.
    """
    def __init__(
            self,
            visitor: 'BaseFactoryVisitor',
            subject: List,
    ):
        EncapsulationBase.__init__(
            self,
            visitor,
            subject
        )

    @property
    def subject(self) -> List:
        return self._subject

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
        decapsulated_value = self._remove_template_class(item)
        if decapsulated_value not in self:
            message = 'item not in list'
            logger.error(message)
            raise KeyError(message)
        self.subject.remove(decapsulated_value)

    def __getitem__(self, index):
        item: Info = self.subject[index]
        return item.accept(self._visitor)

    def __setitem__(self, index, value: Info):
        decapsulated_value = self._remove_template_class(value)
        self.subject[index] = decapsulated_value
        decapsulated_value.parent = self.subject

    def __contains__(self, item: Info):
        decapsulated_value = self._remove_template_class(item)
        return decapsulated_value in self.subject

    def __repr__(self):
        return f'ListEncapsulationBase({self.subject.__repr__()})'
