import logging

from src.black_fennec.structure.structure import Structure

logger = logging.getLogger(__name__)


class List(Structure):
    """Core type List, a list of Structures"""

    def __init__(self, value: list = None):
        """Constructor for List.

        Args:
            data (list[Structure], optional): Structures
                with which to initialise the List.
        """
        Structure.__init__(self)
        self._value = []
        if value is not None:
            self.value = value

    @property
    def value(self):
        return list(self._value)

    @value.setter
    def value(self, value: list):
        for item in (list(self._value) or []):
            self.remove_item(item)
        for item in (value or []):
            self.add_item(item)

    def _set_parent(self, item):
        assert item.parent is None
        item.parent = self

    def add_item(self, item: Structure):
        """Append item to list.

        Args:
            item (Structure): Item to append.
        """
        self._value.append(item)
        self._set_parent(item)

    def _unset_parent(self, item):
        assert item.parent is self
        assert item not in self._value
        item.parent = None

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

    def accept(self, visitor):
        return visitor.visit_list(self)
