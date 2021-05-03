# -*- coding: utf-8 -*-
import logging

from src.structure.info import Info
from src.structure.list import List
from src.structure.overlay.overlay_base import OverlayBase
from src.structure.reference import Reference

logger = logging.getLogger(__name__)


class ListOverlay(OverlayBase, List):
    def __init__(self, subject: List, overlay_factory):
        OverlayBase.__init__(self, subject, overlay_factory)

    @property
    def subject(self) -> List:
        return self._subject

    @property
    def children(self) -> [OverlayBase]:
        """Property for children of this info.
        Returns:
            [ListTemplate]: Empty list
        """
        result: list = list()
        for child in self.subject.children:
            if isinstance(child, Reference):
                reference: Reference = child
                result.append(
                    self._overlay_factory.create(reference.destination)
                )
            else:
                result.append(self._overlay_factory.create(child))
        return result

    def append(self, item: Info):
        """Append item to list template.

        Args:
            item (Info): Item to append.
        """
        decapsulated_item = self._remove_overlay_class(item)
        self.subject.append(decapsulated_item)

    def remove(self, item: Info):
        """Remove item from List.

        Args:
            item (Info): Item to remove.

        Raises:
            KeyError: If the item passed is not in
                list and hence cannot be removed.
        """
        decapsulated_item = self._remove_overlay_class(item)
        if decapsulated_item not in self:
            message = 'item not in list'
            logger.error(message)
            raise KeyError(message)
        self.subject.remove(decapsulated_item)

    def __getitem__(self, index):
        item = self.subject[index]
        return self._overlay_factory.create(item)

    def __setitem__(self, index, value):
        self.subject[index] = self._remove_overlay_class(value)

    def __contains__(self, item):
        decapsulated_value = self._remove_overlay_class(item)
        return decapsulated_value in self.subject

    def __repr__(self):
        return f'ListOverlay({self.subject.__repr__()})'
