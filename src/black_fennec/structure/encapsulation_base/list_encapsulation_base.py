# -*- coding: utf-8 -*-
import logging

from src.black_fennec.structure.encapsulation_base.encapsulation_base import EncapsulationBase
from src.black_fennec.structure.list import List
from src.black_fennec.structure.structure import Structure

logger = logging.getLogger(__name__)


class ListEncapsulationBase(EncapsulationBase, List):
    """Base Class for ecapsulations of a List.

    Contains List specific overrides of certain functions
        to ensure the encapsulation of any Structure returned
        in order to stay in the encapsulation layer.
    """
    def __init__(
            self,
            visitor: 'BaseFactoryVisitor',
            subject: List,
    ):
        List.__init__(self)
        EncapsulationBase.__init__(
            self,
            visitor,
            subject
        )

    @property
    def subject(self) -> List:
        return self._subject

    @property
    def value(self):
        return [item.accept(self._visitor) for item in self.subject.value]

    @value.setter
    def value(self, value):
        self.subject.value = [
            self._remove_template_class(item) for item in value
        ]

    def add_item(self, item: Structure):
        """Append item to list template.

        Args:
            item (Structure): Item to append.
        """
        decapsulated_item = self._remove_template_class(item)
        self.subject.add_item(decapsulated_item)

    def remove_item(self, item: Structure):
        """Remove item from List.

        Args:
            item (Structure): Item to remove.

        Raises:
            KeyError: If the item passed is not in
                list and hence cannot be removed.
        """
        decapsulated_value = self._remove_template_class(item)
        if decapsulated_value not in self.subject.value:
            message = 'item not in list'
            logger.error(message)
            raise KeyError(message)
        self.subject.remove_item(decapsulated_value)

    def __repr__(self):
        return f'ListEncapsulationBase({self.subject.__repr__()})'
