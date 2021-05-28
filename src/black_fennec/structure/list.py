import logging

from src.black_fennec.structure.structure import Structure

logger = logging.getLogger(__name__)


class List(Structure):
    """Core type List, a list of Structures"""

    def __init__(self, value: list = None):
        """Constructor for List.

        Args:
            data (list[Structure], optional): Structures with which to initialise
                the List.
        """
        Structure.__init__(self)
        self._value = list()
        self.value = value

    @property
    def value(self):
        return list(self._value)

    @value.setter
    def value(self, value: list):
        if value:
            for item in value:
                self.add_item(item)

    def add_item(self, item: Structure):
        """Append item to list.

        Args:
            item (Structure): Item to append.
        """
        self._value.append(item)
        self._set_parent(item)

    def _set_parent(self, item):
        if item.parent is not None:
            message = "item already has a parent {}; {}".format(
                item.parent, self)
            logger.error(message)
            raise ValueError(message)
        item.parent = self

    def remove_item(self, item: Structure):
        """Remove item from List.

        Args:
            item (Structure): Item to remove.

        Raises:
            KeyError: If the item passed is not in
                list and hence cannot be removed.
        """
        self._value.remove(item)
        self._unset_parent(item)

    def _unset_parent(self, item):
        assert item.parent is self
        assert item not in self._value
        item.parent = None

    def accept(self, visitor):
        return visitor.visit_list(self)
