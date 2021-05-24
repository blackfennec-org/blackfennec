from collections import UserDict
import logging
from src.black_fennec.structure.structure import Structure

logger = logging.getLogger(__name__)


class Map(Structure, UserDict):
    """Core type Map, a set of keys with values"""

    def __init__(self, data: dict = None):
        """Constructor for List.

        Args:
            data (dict[any, Structure], optional): Structures with which to initialise
                the Map.
        """
        Structure.__init__(self)
        UserDict.__init__(self, data)

    @property
    def value(self) -> dict:
        return dict(self.data)

    @value.setter
    def value(self, value: dict):
        self.data = value

    def __delitem__(self, key):
        """Custom delete hook, resets parent for removed structure.

        Args:
            key (any): The key of the item to delete.

        Raises:
            KeyError: If the item with the key to delete
                is not contained in map.
        """
        try:
            value = self.data.pop(key)
            value.parent = None
        except KeyError as key_error:
            logger.error(key_error)
            raise key_error

    def __setitem__(self, key, value: Structure):
        """Custom set item hook, adds self as parent or raises error.

        Args:
            key: The key for the inserted item.
            value (:obj:`Structure`): The item which will be inserted.

        Raises:
            ValueError: If the item already has a parent.
        """
        if value.parent is not None:
            message = "item already has a parent {}; {}".format(
                value.parent, self)
            logger.error(message)
            raise ValueError(message)
        value.parent = self
        self.data[key] = value

    def accept(self, visitor):
        return visitor.visit_map(self)
