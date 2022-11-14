import logging
from typing import TypeVar

from blackfennec.structure.structure import Structure
from blackfennec.structure.visitor import Visitor
from blackfennec.util.change_notification import ChangeNotification

logger = logging.getLogger(__name__)
T = TypeVar('T', bound=Structure)
TDict = dict[str, T]
TVisitor = TypeVar('TVisitor')


class Map(Structure[TDict]):
    """Core type Map, a set of keys with values"""

    def __init__(self, value: TDict = None):
        """Constructor for List.

        Args:
            value (dict[any, Structure], optional):
                Structures with which to initialise the Map.
        """
        super().__init__()
        self._value: TDict = {}
        if value is not None:
            self.value = value

    @property
    def value(self) -> TDict:
        return dict(self._value)

    @value.setter
    def value(self, value: TDict) -> None:
        notification = ChangeNotification(self.value, value)

        for key in (dict(self._value) or {}):
            self._remove_item(key)
        for key, item in (value or {}).items():
            self._add_item(key, item)

        self._notify('changed', notification)

    def _set_parent(self, item: T) -> None:
        assert item.parent is None
        item.parent = self

    def add_item(self, key: str, value: T) -> None:
        """Custom set item hook, adds self as parent or raises error.

        Args:
            key (str): The key for the inserted item.
            value (Structure): The item which will be inserted.

        Raises:
            ValueError: If the key already exists
        """
        notification = ChangeNotification(self.value, None)

        self._add_item(key, value)

        notification.new_value = self.value
        self._notify('changed', notification)

    def _add_item(self, key: str, value: T) -> None:
        if key in self._value:
            message = f'item already exists {self._value[key]}'
            logger.error(message)
            raise ValueError(message)
        self._set_parent(value)
        self._value[key] = value

    def _is_item(self, item: T) -> bool:
        for i in self._value.items():
            if item is i:
                return True
        return False

    def _unset_parent(self, item: T) -> None:
        assert item.parent is self
        assert not self._is_item(item)
        item.parent = None

    def remove_item(self, key: str) -> None:
        """Custom delete hook, resets parent for removed structure.

        Args:
            key (any): The key of the item to delete.

        Raises:
            KeyError: If the item with the key to delete
                is not contained in map.
        """
        notification = ChangeNotification(self.value, None)

        self._remove_item(key)

        notification.new_value = self.value
        self._notify('changed', notification)

    def _remove_item(self, key: str) -> None:
        if key in self._value:
            value = self._value.pop(key)
            self._unset_parent(value)
        else:
            message = f'item with key({key}) does not exist and thus ' \
                      f'cannot be removed'
            logger.error(message)
            raise KeyError(message)

    def accept(self, visitor: Visitor[TVisitor]) -> TVisitor:
        return visitor.visit_map(self)

    def __repr__(self) -> str:
        """Create representation for pretty printing"""
        return f'Map({self.value})'
