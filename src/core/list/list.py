from collections import UserList
import logging
from src.core.info import Info

logger = logging.getLogger(__name__)


class List(Info, UserList):
    """Core type List, a list of :obj:`Info`s"""

    def __init__(self, data: list = None):
        Info.__init__(self)
        UserList.__init__(self)
        if data:
            for item in data:
                self.append(item)

    @property
    def children(self):
        return list(self.data)

    def _set_parent(self, item):
        if item.parent is not None:
            message = "value already has a parent {}; {}".format(
                item.parent, self)
            logger.error(message)
            raise ValueError(message)
        item.parent = self

    def _unset_parent(self, item):
        assert item.parent is self
        item.parent = None

    def append(self, item):
        super().append(item)
        self._set_parent(item)

    def remove(self, item):
        if item not in self:
            message = "item not in list"
            logger.error(message)
            raise KeyError(message)
        super().remove(item)
        self._unset_parent(item)

    def __delitem__(self, index):
        """Custom delete hook, resets parent for removed info."""
        if index not in range(len(self)):
            message = "index not in bounds of list"
            logger.error(message)
            raise KeyError(message)
        item = self.data.pop(index)
        self._unset_parent(item)

    def __setitem__(self, key, item: Info):
        """Custom set item hook, adds self as parent or raises error.

        Args:
            key: The key for the inserted value.
            value (:obj:`Info`): The value which will be inserted.
        """
        self._set_parent(item)
        self._unset_parent(self.data[key])
        self.data[key] = item
