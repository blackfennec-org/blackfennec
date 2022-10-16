import logging
from typing import TypeVar

from src.black_fennec.structure.structure import Structure
from src.black_fennec.structure.visitor import Visitor

logger = logging.getLogger(__name__)
T = TypeVar('T', bound=Structure)
TVisitor = TypeVar('TVisitor')


class List(Structure[list[T]]):
    """Core type List, a list of Structures"""

    def __init__(self, value: list[T] = None):
        """Constructor for List.

        Args:
            data (list[Structure], optional): Structures
                with which to initialise the List.
        """
        super().__init__()
        self._value: list[T] = []
        if value is not None:
            self.value = value

    @property
    def value(self) -> list[T]:
        return list(self._value)

    @value.setter
    def value(self, value: list[T]) -> None:
        for item in (list(self._value) or []):
            self.remove_item(item)
        for item in (value or []):
            self.add_item(item)

    def _set_parent(self, item: Structure) -> None:
        assert item.parent is None
        item.parent = self

    def add_item(self, item: T) -> None:
        """Append item to list.

        Args:
            item (Structure): Item to append.
        """
        self._set_parent(item)
        self._value.append(item)

    def _is_item(self, item):
        for i in self._value:
            if item is i:
                return True
        return False

    def _unset_parent(self, item: T) -> None:
        assert item.parent is self
        assert not self._is_item(item)
        item.parent = None

    def remove_item(self, item: T) -> None:
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
