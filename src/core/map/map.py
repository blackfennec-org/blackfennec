from collections import UserDict
import logging
from src.core.info import Info

logger = logging.getLogger(__name__)

class Map(Info, UserDict):
    """Core type Map, a set of keys with values"""

    def __init__(self):
        Info.__init__(self)
        UserDict.__init__(self)

    def __delitem__(self, key):
        """Custom delete hook, resets parent for removed info."""
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
        """
        if value.parent is not None:
            message = "value already has a parent {}; {}".format(
                value.parent, self)
            logger.error(message)
            raise ValueError(message)
        value.parent = self
        self.data[key] = value
