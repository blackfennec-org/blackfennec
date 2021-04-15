from src.core.info import Info


class MapViewModel:
    """View model for core type Map."""

    def __init__(self, interpretation):
        """Create with value empty map.

        Args:
            interpretation (:obj:`Interpretation`): The overarching
                interpretation
        """
        self._interpretation = interpretation
        self._map = self._interpretation.info
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

    def navigate_to(self, route_target: Info):
        self._interpretation.navigate(route_target)
