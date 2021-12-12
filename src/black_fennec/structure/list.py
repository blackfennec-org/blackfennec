import logging
from typing import TypeVar

from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.visitor import Visitor

logger = logging.getLogger(__name__)
TVisitor = TypeVar('TVisitor')


class List(Structure[list]):
    """Core type List, a list of Structures"""

    def __init__(self, value: list = None):
        """Constructor for List.

        Args:
            data (list[Structure], optional): Structures
                with which to initialise the List.
        """
        Structure.__init__(self, [])
        if value is not None:
            self.value = value

    @property
    def value(self) -> list:
        return list(self._value)

    @value.setter
    def value(self, value: list) -> None:
        for item in (list(self._value) or []):
            self.remove_item(item)
        for item in (value or []):
            self.add_item(item)

    def _set_parent(self, item: Structure) -> None:
        assert item.parent is None
        item.parent = self

    def add_item(self, item: Structure) -> None:
        """Append item to list.

        Args:
            item (Structure): Item to append.
        """
        self._value.append(item)
        self._set_parent(item)

    def _unset_parent(self, item: Structure) -> None:
        assert item.parent is self
        assert item not in self._value
        item.parent = None

    def remove_item(self, item: Structure) -> None:
        """Remove item from List.

        Args:
            item (Structure): Item to remove.

        Raises:
            KeyError: If the item passed is not in
                list and hence cannot be removed.
        """
        self._value.remove(item)
        self._unset_parent(item)

    def accept(self, visitor: Visitor[TVisitor]) -> TVisitor:
        return visitor.visit_list(self)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f'List({self.value})'
