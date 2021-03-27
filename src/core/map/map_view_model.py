from src.core.info import Info
from src.core.map import Map

class MapViewModel:
    """View model for core type String."""

    def __init__(self, interpretation):
        """Create with value empty string.

        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation
        """
        self._map = Map()

    @property
    def value(self):
        """Readonly property for value."""
        return self._map

    def add_item(self, key, value: Info):
        """Add item (key, value) to the map.

        Args:
            key: The key under which to store the value.
            value (:obj:`Info`): The `Info` behind the key.
        """
        self._map[key] = value

    def delete_item(self, key):
        """Delete an item from the map.

        Args:
            key: The key of the key value pair which should be deleted
        """
        self._map.pop(key)
