import logging
from collections import UserList
from src.black_fennec.structure.structure import Structure

logger = logging.getLogger(__name__)


class List(Structure, UserList):
    """Core type List, a list of Structures"""

    def __init__(self, data: list= None):
        """Constructor for List.

        Args:
            data (list[Structure], optional): Structures with which to initialise
                the List.
        """
        Structure.__init__(self)
        UserList.__init__(self)
        if data:
            for item in data:
                self.append(item)

    @property
    def value(self):
        return list(self.data)

    @value.setter
    def value(self, value: list):
        self.data = value

    def _set_parent(self, item):
        """Helper method to set parent of item

        Args
            item (Structure): Item on which to set parent to `self`.
        """
        if item.parent is not None:
            message = "item already has a parent {}; {}".format(
                item.parent, self)
            logger.error(message)
            raise ValueError(message)
        item.parent = self

    def _unset_parent(self, item):
        assert item.parent is self
        item.parent = None

    def append(self, item: Structure):
        """Append item to list.

        Args:
            item (Structure): Item to append.
        """
        super().append(item)
        self._set_parent(item)

    def remove(self, item: Structure):
        """Remove item from List.

        Args:
            item (Structure): Item to remove.

        Raises:
            KeyError: If the item passed is not in
                list and hence cannot be removed.
        """
        if item not in self:
            message = "item not in list"
            logger.error(message)
            raise KeyError(message)
        super().remove(item)
        self._unset_parent(item)

    def __delitem__(self, index):
        """Custom delete hook, resets parent for removed structure."""
        if index not in range(len(self)):
            message = "index not in bounds of list"
            logger.error(message)
            raise KeyError(message)
        item = self.data.pop(index)
        self._unset_parent(item)

    def __setitem__(self, key, item: Structure):
        """Custom set item hook, adds self as parent or raises error.

        Args:
            key: The key for the inserted item.
            item (Structure): The item which will be inserted.
        """
        self._set_parent(item)
        self._unset_parent(self.data[key])
        self.data[key] = item

    def accept(self, visitor):
        return visitor.visit_list(self)
