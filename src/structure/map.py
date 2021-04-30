from collections import UserDict
import logging
from src.structure.info import Info

logger = logging.getLogger(__name__)


class Map(Info, UserDict):
    """Core type Map, a set of keys with values"""

    def __init__(self, data: dict = None):
        """Constructor for List.

        Args:
            data (dict[any, Info], optional): Infos with which to initialise
                the Map.
        """
        Info.__init__(self)
        UserDict.__init__(self, data)

    @property
    def children(self):
        """Readonly property for child infos"""
        return list(self.data.values())

    def __delitem__(self, key):
        """Custom delete hook, resets parent for removed info.

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

    def __setitem__(self, key, value: Info):
        """Custom set item hook, adds self as parent or raises error.

        Args:
            key: The key for the inserted value.
            value (:obj:`Info`): The value which will be inserted.

        Raises:
            ValueError: If the item already has a parent.
        """
        if value.parent is not None:
            message = "value already has a parent {}; {}".format(
                value.parent, self)
            logger.error(message)
            raise ValueError(message)
        value.parent = self
        self.data[key] = value
