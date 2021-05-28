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
        self._value = dict()
        self.value = value

    @property
    def value(self) -> dict:
        return dict(self._value)

    @value.setter
    def value(self, value: dict):
        for key in dict(self._value):
            self.remove_item(key)
        if value:
            for key, value in value.items():
                self.add_item(key, value)

    def remove_item(self, key):
        """Custom delete hook, resets parent for removed structure.

        Args:
            key (any): The key of the item to delete.

        Raises:
            KeyError: If the item with the key to delete
                is not contained in map.
        """
        try:
            value = self._value.pop(key)
            value.parent = None
        except KeyError as key_error:
            logger.error(key_error)
            raise key_error

    def add_item(self, key, value: Structure):
        """Custom set item hook, adds self as parent or raises error.

        Args:
            key: The key for the inserted item.
            value (:obj:`Structure`): The item which will be inserted.

        Raises:
            ValueError: If the item already has a parent.
        """
        if value.parent is not None:
            message = f"item already has a parent {value.parent}; {self}"
            logger.error(message)
            raise ValueError(message)
        value.parent = self
        if key in self._value:
            message = f"item already exists {self._value[key]}"
            logger.error(message)
            raise ValueError(message)
        self._value[key] = value

    def accept(self, visitor):
        return visitor.visit_map(self)
