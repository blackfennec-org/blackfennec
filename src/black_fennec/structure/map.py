import logging

from src.black_fennec.structure.structure import Structure

logger = logging.getLogger(__name__)


class Map(Structure):
    """Core type Map, a set of keys with values"""

    def __init__(self, value: dict = None):
        """Constructor for List.

        Args:
            value (dict[any, Structure], optional):
                Structures with which to initialise the Map.
        """
        Structure.__init__(self)
        self._value = {}
        if value is not None:
            self.value = value

    @property
    def value(self) -> dict:
        return dict(self._value)

    @value.setter
    def value(self, value: dict):
        for key in (dict(self._value) or {}):
            self.remove_item(key)
        for key, item in (value or {}).items():
            self.add_item(key, item)

    def _set_parent(self, item):
        assert item.parent is None
        item.parent = self

    def add_item(self, key: str, value: Structure):
        """Custom set item hook, adds self as parent or raises error.

        Args:
            key (str): The key for the inserted item.
            value (Structure): The item which will be inserted.

        Raises:
            ValueError: If the key already exists
        """
        if key in self._value:
            message = f'item already exists {self._value[key]}'
            logger.error(message)
            raise ValueError(message)
        self._set_parent(value)
        self._value[key] = value

    def _unset_parent(self, item):
        assert item.parent is self
        assert item not in self._value
        item.parent = None

    def remove_item(self, key):
        """Custom delete hook, resets parent for removed structure.

        Args:
            key (any): The key of the item to delete.

        Raises:
            KeyError: If the item with the key to delete
                is not contained in map.
        """
        if key in self._value:
            value = self._value.pop(key)
            self._unset_parent(value)
        else:
            message = f'item with key({key}) does not exist and thus ' \
                      f'cannot be removed'
            logger.error(message)
            raise KeyError(message)

    def accept(self, visitor):
        return visitor.visit_map(self)
